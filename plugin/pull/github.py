#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

import base
from objects import github


class GitHubPlugin(base.PullPlugin):

    def __call__(self, *args, **kwargs):
        content = self.get_github_repo_content()
        return content

    def get_github_repo_content(self):
        github_repositories = []
        results = self.get_github_repos()
        if results and results.get("items", None):
            for item in results['items']:
                g = github.GitHubRepo()
                g.from_dict(item)
                github_repositories.append(g)
        repo_content = github.GithubRepoContent(github_repositories)
        return repo_content

    def get_github_repos(self, language='python', sort='stars', order='desc', page='1', per_page='10'):
        # get python top 10 stared repositories
        base_url = 'https://api.github.com/search/repositories'
        params_url = '?q=language:%s&sort=%s&order=%s&page=%s&per_page=%s' % (language, sort, order, page, per_page)
        r = requests.get(base_url + params_url)
        if r.status_code == 200:
            print 'get github repositories success.'
            return r.json()
        else:
            print 'get github repositories error.'
