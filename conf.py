#!/usr/bin/python
# -*- coding: UTF-8 -*-
from config import pull_plugins
from config import push_plugins

CONF = {}


def register_all():
    for key in pull_plugins.plugins:
        CONF[key] = pull_plugins.plugins[key]
    for key in push_plugins.plugins:
        CONF[key] = push_plugins.plugins[key]


register_all()
