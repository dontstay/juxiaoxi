#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base


class BlogContent(base.BaseContent):
    extend_keys = ['blog_name']

    def __init__(self):
        super(BlogContent, self).__init__()
