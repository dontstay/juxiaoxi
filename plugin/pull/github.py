import requests

import base


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


class GitHubPlugin(base.PullPlugin):

    def __call__(self, *args, **kwargs):
        # get python top 10 stared repositories
        github_repositories = []
        results = self.get_github_repositories()
        if results and results.get("items", None):
            for item in results['items']:
                g = GitHubRepo()
                g.from_dict(item)
                github_repositories.append(g)
        return self.format_content(github_repositories)

    def get_github_repositories(self, language='python', sort='stars', order='desc', page='1', per_page='10'):
        base_url = 'https://api.github.com/search/repositories'
        params_url = '?q=language:%s&sort=%s&order=%s&page=%s&per_page=%s' % (language, sort, order, page, per_page)
        r = requests.get(base_url + params_url)
        if r.status_code == 200:
            print 'get github repositories success.'
            return r.json()
        else:
            print 'get github repositories error.'

    def format_content(self, content):
        result = u"---\nlayout: post\ntitle: github python TOP 10 热门项目\ndescription: github python TOP 10 热门项目\ncategory: github\n---\n"
        for cont in content:
            t = cont.to_dict()
            for key in cont.all_keys:
                if key == 'name':
                    result += "## %s \n" % t.get(key, '')
                elif key in ['html_url']:
                    result += "- **%s**: [%s](%s) \n\n" % (key, t.get(key, ''), t.get(key, ''))
                else:
                    result += "- **%s**: `%s` \n" % (key, t.get(key, ''))
        return result
