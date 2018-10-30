#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base


class BlogContent(base.BaseObject):
    
    def __init__(self):
        self.all_keys = ['title', 'body', 'category', 'blog_name']
        super(BlogContent, self).__init__()
