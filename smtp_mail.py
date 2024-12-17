



# import the installed Jira library
from jira import JIRA

# Specify a server key. It should be your
# domain name link. yourdomainname.atlassian.net
jiraOptions = {'server': "https://kumargautam41098.atlassian.net"}
api_token = "ATATT3xFfGF0kFwTbrHUbkWYKhBR3qEiNREAgXdwPbh2rB-QWb4Zt3YgiD0WHgMzeHdtlIzeQqmAYPHXd_rvwAQZA-rdSRnB_SH9VyHagzVJAlPyQvwJWDN9jIC5GcDxNouDpFqEwpu7zT1jvTFUvufWaHMv3DxBd5NmuxCqZHlerru1vuSdw84=B212E125"
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
