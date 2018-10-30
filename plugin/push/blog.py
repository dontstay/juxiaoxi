#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import date
import os

import base
from common import utils


class BlogPlugin(base.PushPlugin):

    def __call__(self, data, *args, **kwargs):
        try:
            print "git pull..."
            os.system("cd /root/dontstay.github.io; git pull ")
            d = date.today()
            file_name = "/root/dontstay.github.io/_posts/" + data.category + "/" + str(
                d.isoformat()) + "-" + data.blog_name + ".md"
            print "write file..., ", file_name
            utils.write_content_to_file(data.body, file_name)
        except Exception as ex:
            print "%s" % ex
            return
        print "git push blog..."
        os.system("cd /root/dontstay.github.io; git add --all; git commit -m 'add new blog'; git push origin master ")
