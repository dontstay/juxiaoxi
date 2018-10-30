#!/usr/bin/python
# -*- coding: UTF-8 -*-
import blog
from datetime import date


class GitHubRepo(object):
    all_keys = ['name',
                'language',
                'forks',
                'watchers',
                'created_at',
                'description',
                'html_url'
                ]

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


class GithubRepoContent(object):

    def __init__(self, content):
        self.content = content

    def to_blog(self):
        d = date.today()
        title = str(d.year) + u"年" + str(d.month) + u"月 python TOP10 项目"
        body = u"---\nlayout: post\ntitle: " + title + "\ndescription: " + title + "\ncategory: github\n---\n"
        for cont in self.content:
            t = cont.to_dict()
            for key in cont.all_keys:
                if key == 'name':
                    body += "## %s \n" % t.get(key, '')
                elif key in ['html_url']:
                    body += "- **%s**: [%s](%s) \n\n" % (key, t.get(key, ''), t.get(key, ''))
                else:
                    body += "- **%s**: %s \n" % (key, t.get(key, ''))
        b = blog.BlogContent()
        b.title = title
        b.body = body
        b.blog_name = "github-top-stared-python-projects"
        return b
