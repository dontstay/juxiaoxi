from conf import CONF
from common import utils


def go(users):
    for usr in users:
        print usr
        user_pull = users[usr]['pull'].split(',')
        pull_content = {}
        if user_pull:
            for pull in user_pull:
                pull_key = 'pull.' + pull
                print pull_key
                pull_class = CONF.get(pull_key, None)
                print pull_class
                if pull_class:
                    pull_class_obj = utils.import_class(pull_class)
                    pull_clazz = pull_class_obj()
                    pull_result = pull_clazz()
                    pull_content[pull_key] = pull_result
        user_push = users[usr]['push'].split(',')
        if pull_content and user_push:
            for pull_key in pull_content:
                for push in user_push:
                    push_key = 'push.' + push
                    print push_key
                    push_class = CONF.get(push_key, None)
                    print push_class
                    if push_class:
                        push_class_obj = utils.import_class(push_class)
                        push_clazz = push_class_obj()
                        push_clazz(pull_content[pull_key])
