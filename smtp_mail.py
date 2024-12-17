



# import the installed Jira library
from jira import JIRA

# Specify a server key. It should be your
# domain name link. yourdomainname.atlassian.net
jiraOptions = {'server': "https://kumargautam41098.atlassian.net"}

# Get a JIRA client instance, pass,
# Authentication parameters
# and the Server name.
# emailID = your emailID
# token = token you receive after registration
jira = JIRA(options=jiraOptions, basic_auth=(
    "kumar.gautam41098@gmail.com", api_token))

# Search all issues mentioned against a project name.
for singleIssue in jira.search_issues(jql_str='project = testing_project'):
  print(singleIssue)
  print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary,\
                             singleIssue.fields.reporter.displayName))


print(jira)
