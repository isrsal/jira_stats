# coding: utf-8
from jira import JIRA
from itertools import groupby

user_name=""
pasword=""
project="Data"

jira = JIRA("https://eyeview.atlassian.net",basic_auth=(user_name, pasword))
issues = jira.search_issues('project=%s and sprint in openSprints ()' % project, maxResults=500)
x=[(i.fields.status.name, i.fields.customfield_10004) for i in issues]
x.sort()
y=groupby(x,key = lambda x:x[0])
for key, rows in y:
    print key, sum(r[1] for r in rows if r[1] is not None)
