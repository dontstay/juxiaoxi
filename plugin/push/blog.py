import os

import base

"""
1.blog environment must install node js, https://hexo.io/zh-cn/docs/index.html
2.install hexo at https://github.com/hexojs/hexo
3.install hexo plugin hexo-deployer-git
4.download blog code https://github.com/dontstay/dontstay
5.hexo new "Hello Hexo"
6.hexo generate
7.hexo deploy

"""


class BlogPlugin(base.PushPlugin):

    def __call__(self, *args, **kwargs):
        os.system("cd /root/dontstay; hexo new github_python_projects")
        os.system("cd /root/dontstay; hexo generate ")
        os.system("cd /root/dontstay; hexo deploy ")
