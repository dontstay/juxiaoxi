#!/usr/bin/python
# -*- coding: UTF-8 -*-
from objects import base
import blog


class Rss(base.BaseObject):

    def __init__(self):
        self.all_keys = ['url', 'title', 'author_name', 'author_uri', 'published', 'content']
        super(Rss, self).__init__()


class RssContent(object):

    def __init__(self, config):
        self.config = config

    def to_blog(self):
        body = u"---\nlayout: post\ntitle: " + self.config['title'] + "\ndescription: " + self.config[
            'title'] + "\ncategory: " + self.config['category'] + "\n---\n"
        for cont in self.config['content']:
            t = cont.to_dict()
            body += u"## [%s](%s) \n" % (t.get('title', ''), t.get('url', ''))
            body += u"作者： [%s](%s) 发表于：%s \n" % (t.get('author_name', ''), t.get('author_uri', ''), t.get('published', ''))
            body += u"%s \n\n" % t.get('content', '')
        b = blog.BlogContent()
        b.title = self.config['title']
        b.category = self.config['category']
        b.body = body
        b.blog_name = self.config['blog_name']
        return b
