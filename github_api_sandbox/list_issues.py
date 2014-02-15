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

for a in gh.iter_issues():
    print '%s - %s' % (a.repository[1], a.title)
