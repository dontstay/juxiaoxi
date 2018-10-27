from datetime import date
import os

import base
from common import utils


class BlogPlugin(base.PushPlugin):

    def __call__(self, data, *args, **kwargs):
        d = date.today()
        try:
            print "write file..."
            utils.write_content_to_file(data, "/root/dontstay.github.io/_posts/github/"+str(d.isoformat())+"-github-top-stared-python-projects.md")
        except Exception as ex:
            print "%s" % ex
            return
        print "git push blog"
        os.system("cd /root/dontstay.github.io; git add --all; git commit -m 'add new blog'; git push origin master ")
