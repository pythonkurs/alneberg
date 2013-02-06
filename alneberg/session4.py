import requests

def do_this():
    with open("/home/johannes/secret") as secret:
        password = secret.read().strip()
        
    repos = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=("alneberg", password))
    repos_data = repos.json()
    for repo in repos_data:
        git_commits_url = repo[u'commits_url'][0:-6]
        commits = requests.get(git_commits_url, auth=("alneberg", password))
        commits_data = commits.json()
        for commit in commits_data:
            print commit['commit']['message'], commit['commit']['author']['date']

