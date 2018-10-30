#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import date
import os

import base
from common import utils


class BlogPlugin(base.PushPlugin):

    def __call__(self, data, *args, **kwargs):
        try:
            print "write file..."
            os.system("cd /root/dontstay.github.io; git pull ")
            d = date.today()
            file_name = "/root/dontstay.github.io/_posts/github/"+str(d.isoformat())+"-"+data.blog_name+".md"
            utils.write_content_to_file(data.body, file_name)
        except Exception as ex:
            print "%s" % ex
            return
        print "git push blog"
        os.system("cd /root/dontstay.github.io; git add --all; git commit -m 'add new blog'; git push origin master ")
