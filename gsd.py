#! ./venv/bin/python

##############
# TEMP/DEBUG
debug_on = True
##############

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


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = 'ransage'

pw = getpass.getpass();  

gh = login(username, password=pw)

repo_pers = gh.repository(owner='ransage',repository='R_personal')

repo = repo_pers  # TODO allow user to select repo



import readline
import shlex


def help_string():
    return '''
Help:

new title_str [body_str [label_nums_list]] 

 - substitute 'nd' for 'new' for new deferred action
 - 'n' can be used for 'new'

Example:
n 'Organize closet' '' '3,6' # Creates task with no body and two labels
'''

def get_milestone_num(milestone_text):
    # Todo - revise this to not be hard-coded
    if milestone_text in ('action','actionable'):
        return 1
    elif milestone_text in ('defer','deferred'):
        return 2
    else:
        return None

def create_new_issue(arg_list, milestone_text='action'):
    title_string = 'Wrap an interface around '
    body_string_preface = '''WARNING: python auto-generated this text and it is likely to get edited and/or deleted.
Use comments if you want to append information to this issue.
--------------------

'''
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
    
    
    close_preface = '''
--------------------
Item closed by python script for reason:
'''

    close_message = '%sPosting this issue makes it successful (lol)' % close_preface

    body_text = ('%s[debug]\n[auto-gen]  \n%s' % 
             (body_string_preface, close_message))
    try:
        z = repo.create_issue(title=title_string)
        if debug_on:
            print('No exception, returned: %s' % str(z))
    except:
        z = None
        if debug_on:
            print('Exception for "%s" - setting to None ' % title_string)
    
    milestone_num = get_milestone_num(milestone_text)


    if(z):
        success = z.edit(body='[debug]\n[auto-gen]',
                         assignee='ransage',
                         milestone=1,
                         labels=['gsd_gtd','urgent_relatively','0_online'])
        if(success):
            print('Success')
        else:
            print('Created following issue with title only:\n  "%s"' % title_string)
    else:
        print('!!! Failed to create issue %s !!!' % title_string)



if __name__ == "__main__":

    print('Enter a command to do something, e.g. `create name price`.')
    print('To get help, enter `help`.')

    while True:
        print('Active project/repo: %s' % repo)

        cmd = shlex.split(raw_input('> '))
        if debug_on:
            print cmd

        if cmd[0] in ('exit','x','quit','q'):
            break
        
        elif cmd[0] in ('help', 'h'):
            print(help_string())
        
        elif cmd[0] in ('new', 'n'):
            create_new_issue(cmd[1:], 'action')
        
        elif cmd[0]=='nd':
            create_new_issue(cmd[1:], 'defer')
        
        # TODO - add option for creating incubate
        
        # ...
        
        else:
            print('Unknown command: {}'.format(cmd))
    print('Done')

print('End of file')

