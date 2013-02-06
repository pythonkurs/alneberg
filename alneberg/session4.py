import requests
from pandas import DataFrame, Series
from dateutil import parser
import datetime
from collections import Counter

def fetch_commits():
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
    return df
#    df.to_csv('mydf.tsv', sep='\t')

def reload_df(file_name):
    df = read_table(file_name)
    return df

def common_commit_times(df):
    weekday_hash = {0: "Monday", 1: "Tuesday",
                    2: "Wednesday", 3: "Thursday",
                    4: "Friday", 5: "Saturday",
                    6: "Sunday"}
    time_list = list(df.index)
    day_list = []
    hour_list = []
    for time_str in time_list:
        time = parser.parse(time_str)
        day_list.append(time.weekday())
        hour_list.append(time.hour)
    c_day = Counter(day_list)
    c_hour = Counter(hour_list)
    day_name = weekday_hash[c_day.most_common(1)[0][0]]
    mc_hour = c_hour.most_common(1)[0][0]
    return day_name,mc_hour
