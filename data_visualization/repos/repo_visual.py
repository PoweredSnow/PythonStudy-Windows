import requests

from plotly import offline

class RepoVisual:
    def __init__(self, language):
        self.language = language

    def start(self):
        self.dealWithRequest()

    def getApi(self):
        url = f'https://api.github.com/search/repositories?q=language:{self.language}&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)
        print(f"Status code: {r.status_code}")
        return r.json()

    def dealWithRequest(self):
        response_dict = self.getApi()
        repo_dicts = response_dict['items']
        repo_links, stars, labels = [], [], []
        for repo_dict in repo_dicts:
            repo_name = repo_dict['name']
            repo_url = repo_dict['html_url']
            repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
            repo_links.append(repo_link)
            stars.append(repo_dict['stargazers_count'])
            owner = repo_dict['owner']['login']
            description = repo_dict['description']
            label = f"{owner}<br />{description}"
            labels.append(label)
        self.repoVisual(repo_links, stars, labels)

    def repoVisual(self, repo_links, stars, labels):
        data = [{
            'type': 'bar',
            'x': repo_links,
            'y': stars,
            'hovertext': labels,
            'marker': {
                'color': 'rgb(60, 100, 150)',
                'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
            },
            'opacity': 0.6,
        }]
        my_layout = {
            'title': f'Github 上最受欢迎的 {self.language} 项目',
            'xaxis': {
                'title': 'Repository',
                'titlefont': {'size': 24},
                'tickfont': {'size': 14},
            },
            'yaxis': {
                'title': 'Stars',
                'titlefont': {'size': 24},
                'tickfont': {'size': 14},
            },
        }
        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename=f'{self.language}_repos.html')
