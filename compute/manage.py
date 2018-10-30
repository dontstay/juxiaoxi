#!/usr/bin/python
# -*- coding: UTF-8 -*-
from conf import CONF
from common import utils


def go(users):
    # get all plugins
    plugins = {}
    print "get all plugins..."
    for usr in users:
        for pull in users[usr]['pull']:
            plugins[pull] = users[usr]['push'].split(',')
    print "plugins: ", plugins
    # prepare all data
    pull_contents = {}
    print "prepare all data..."
    for pull, pushs in plugins.items():
        pull_key = 'pull.' + pull
        print "pull_key: ", pull_key
        pull_contents[pull_key] = {}
        pull_class = CONF.get(pull_key, None)
        print "pull_class: ", pull_class
        if pull_class:
            pull_class_obj = utils.import_class(pull_class)
            pull_clazz = pull_class_obj()
            for pull_plugin_key in pull_clazz.all_keys:
                print "pull_plugin_key: ", pull_plugin_key
                pull_content = pull_clazz(pull_plugin_key)
                pull_contents[pull_key][pull_plugin_key] = {}
                pull_contents[pull_key][pull_plugin_key]['content'] = pull_content
                if pushs and len(pushs) > 0:
                    for push in pushs:
                        push_key = 'push.' + push
                        print "push_key: ", push_key
                        to_method = getattr(pull_content, "to_"+push)
                        pull_contents[pull_key][pull_plugin_key][push_key] = to_method()
    if not pull_contents:
        print "get empty content."
        return
    # push all data
    print "push all user data..."
    for usr in users:
        print "user: ", usr
        user_pull = users[usr]['pull'].keys()
        user_push = users[usr]['push'].split(',')
        if user_pull and user_push:
            for pull in user_pull:
                pull_key = 'pull.' + pull
                print "pull_key: ", pull_key
                for plugin_key in users[usr]['pull'][pull]:
                    for push in user_push:
                        push_key = 'push.' + push
                        print "push_key: ", push_key
                        push_class = CONF.get(push_key, None)
                        print "push_class: ", push_class
                        if push_class:
                            push_class_obj = utils.import_class(push_class)
                            push_clazz = push_class_obj()
                            push_clazz(pull_contents[pull_key][plugin_key][push_key])
