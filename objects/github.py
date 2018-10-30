#!/usr/bin/python
# -*- coding: UTF-8 -*-
from objects import base
import blog


class GitHubRepo(base.BaseObject):

    def __init__(self):
        self.all_keys = ['name', 'language', 'forks', 'watchers', 'created_at', 'description', 'html_url']
        super(GitHubRepo, self).__init__()


class GithubRepoContent(object):

    def __init__(self, config):
        self.config = config

    def to_blog(self):
        print "format content to blog..."
        body = u"---\nlayout: post\ntitle: " + self.config['title'] + "\ndescription: " + self.config[
            'title'] + "\ncategory: " + self.config['category'] + "\n---\n"
        for cont in self.config['content']:
            t = cont.to_dict()
            for key in cont.all_keys:
                if key == 'name':
                    body += "## %s \n" % t.get(key, '')
                elif key in ['html_url']:
                    body += "- **%s**: [%s](%s) \n\n" % (key, t.get(key, ''), t.get(key, ''))
                else:
                    body += "- **%s**: %s \n" % (key, t.get(key, ''))
        b = blog.BlogContent()
        b.title = self.config['title']
        b.category = self.config['category']
        b.body = body
        b.blog_name = self.config['blog_name']
        return b
