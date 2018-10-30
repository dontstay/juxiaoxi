#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import date
import feedparser

from objects import rss
import base

d = date.today()


class RssPlugin(base.PullPlugin):
    all_keys = {
        "cnblog_picked": {
            "url": "http://feed.cnblogs.com/blog/picked/rss",
            "title": str(d.year) + u"年" + str(d.month) + u"月" + str(d.day) + u"日 博客园 精华区",
            "category": "blogs",
            "blog_name": "cnblog-picked-rss",
            "content": []
        },
        "cnblog_python": {
            "url": "http://feed.cnblogs.com/blog/sitecateogry/python/rss",
            "title": str(d.year) + u"年" + str(d.month) + u"月" + str(d.day) + u"日 博客园 python区",
            "category": "blogs",
            "blog_name": "cnblog-python-rss",
            "content": []
        },
        "cnblog_linux": {
            "url": "http://feed.cnblogs.com/blog/sitecateogry/linux/rss",
            "title": str(d.year) + u"年" + str(d.month) + u"月" + str(d.day) + u"日 博客园 linux区",
            "category": "blogs",
            "blog_name": "cnblog-linux-rss",
            "content": []
        },
    }

    def __call__(self, key, *args, **kwargs):
        content = self.get_rss_content(key)
        return content

    def get_rss_content(self, key):
        rss_contents = []
        print "get rss content..."
        feed = self.get_rss_body(self.all_keys[key]['url'])
        for entry in feed.entries:
            rs = rss.Rss()
            rs.url = entry.id
            rs.title = entry.title
            rs.author_name = entry.authors[0]['name']
            rs.author_uri = entry.authors[0]['href']
            rs.published = entry.published
            rs.content = entry.content[0]['value']
            rss_contents.append(rs)
        self.all_keys[key]['content'] = rss_contents
        rss_content = rss.RssContent(self.all_keys[key])
        return rss_content

    def get_rss_body(self, rss_url):
        body = feedparser.parse(rss_url)
        return body
