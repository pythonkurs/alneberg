import requests
from pandas import DataFrame, Series

def do_this():
    with open("/home/johannes/secret") as secret:
        password = secret.read().strip()
        
    repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=("alneberg", password))
    repos_data = repos.json()
    data_dict = {}
    for repo in repos_data:
        git_commits_url = repo[u'commits_url'][0:-6]
        commits = requests.get(git_commits_url, auth=("alneberg", password))
        commits_data = commits.json()
        commit_list = []
        time_list = []
        author_name = repo['html_url'].split('/')[-1]
        for commit in commits_data:
            commit_list.append(commit['commit']['message'])
            time_list.append(commit['commit']['author']['date'])
        data_dict[author_name] = Series(commit_list, index=time_list)
    df = DataFrame(data_dict)
    print df

