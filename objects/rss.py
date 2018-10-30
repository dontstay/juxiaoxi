#!/usr/bin/python
# -*- coding: UTF-8 -*-
from objects import base
import blog


class Rss(base.BaseObject):

    def __init__(self):
        self.all_keys = ['url', 'title']
        super(Rss, self).__init__()


class RssContent(object):

    def __init__(self, config):
        self.config = config

    def to_blog(self):
        body = u"---\nlayout: post\ntitle: " + self.config['title'] + "\ndescription: " + self.config[
            'title'] + "\ncategory: " + self.config['category'] + "\n---\n"
        for cont in self.config['content']:
            t = cont.to_dict()
            body += "## [%s](%s)" % (t.get('title', ''), t.get('url', ''))
        b = blog.BlogContent()
        b.title = self.config['title']
        b.category = self.config['category']
        b.body = body
        b.blog_name = self.config['blog_name']
        return b
