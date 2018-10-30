#!/usr/bin/python
# -*- coding: UTF-8 -*-


class BaseObject(object):
    all_keys = []

    def __init__(self):
        for key in self.all_keys:
            if not hasattr(self, key):
                setattr(self, key, None)

    def from_dict(self, dic):
        for key, value in dic.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        result = {}
        for key in self.all_keys:
            if hasattr(self, key):
                result[key] = getattr(self, key, None)
        return result
