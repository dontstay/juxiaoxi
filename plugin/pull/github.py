#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import date

import base
from common import utils
from objects import github

d = date.today()


class GitHubPlugin(base.PullPlugin):

    all_keys = {
        "python_stared": {
            "url": "language:python&sort=stars&order=desc&page=1&per_page=20",
            "title": str(d.year) + u"年" + str(d.month) + u"月 python TOP20 项目",
            "category": "sites",
            "blog_name": "github-top-stared-python-projects",
            "content": []
        }
    }

    def __call__(self, key, *args, **kwargs):
        content = self.get_github_repo_content(key)
        return content

    def get_github_repo_content(self, key):
        github_repositories = []
        results = self.get_github_repos(self.all_keys[key]['url'])
        if results and results.get("items", None):
            for item in results['items']:
                g = github.GitHubRepo()
                g.from_dict(item)
                github_repositories.append(g)
        self.all_keys[key]['content'] = github_repositories
        repo_content = github.GithubRepoContent(self.all_keys[key])
        return repo_content

    def get_github_repos(self, params_url):
        base_url = 'https://api.github.com/search/repositories?q='
        body = utils.get_content_by_url(base_url + params_url)
        return body
