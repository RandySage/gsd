#! ../venv/bin/python

import getpass
from github3 import login
import sys

# Server still on Python 2.6.x - defer...
# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('--login', 
#                     help='username for github')
# parser.add_argument('--password', 
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print args


if len(sys.argv) > 2:
    username = sys.argv[1]
    pw = sys.argv[2]
else:
    username = 'ransage'
    pw = getpass.getpass();  

gh = login(username, password=pw)

repo_pers = gh.repository(owner='ransage',repository='R_personal')

title_string = 'Wrap an interface around '
body_string_preface = '''WARNING: python auto-generated this text and it is likely to get edited and/or deleted.
Use comments if you want to append information to this issue.
--------------------

'''


close_preface = '''
--------------------
Item closed by python script for reason:
'''

close_message = '%sPosting this issue makes it successful (lol)' % close_preface

body_text = ('%s[debug]\n[auto-gen]  \n%s' % 
             (body_string_preface, close_message))

#z = repo_pers.create_issue(title=title_string)
z = repo_pers.issue(48)
print('returned: %s' % str(z))
if(z):
    success = z.edit(body='[debug]\n[auto-gen]',
                     assignee='ransage',
                     milestone=1,
                     labels=['gsd_gtd','urgent_relatively','0_online'])
    if(success):
        print 'Success'
    else:
        print 'Fail'
else:
    print('!!! Failed to create issue %s !!!' % title_string)


