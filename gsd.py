#! ./venv/bin/python

##############
# TEMP/DEBUG
debug_on = True
##############

import getpass
from github3 import login
import sys
from thirdparty.query_yes_no import query_yes_no


import json
with open('settings.json') as json_file:
    settings = json.load(json_file)

# GENERAL LIST
# TODO - clean up import locations & syntax


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

 
pw = getpass.getpass("Password for %s: " % username)

gh = login(username, password=pw)

repo_pers = gh.repository(owner='ransage',repository='R_personal')

repo = repo_pers  # TODO allow user to select repo

labels_list = []
def generate_labels_list():
    global labels_list # TODO - Change to class instead of having globals!!!
    labels_list = []
    try:
        for label in repo.iter_labels():
            label_name = label.name
            labels_list.append(label_name)
            if label_name != label_name.lower():
                print('WARNING: Label "%s" is not lowercase!' % label_name)
    except:
        print('generate_labels_list() caught exception - re-throwing')
        raise
    labels_list.sort()


################
# CONSTRUCTOR??
generate_labels_list() # Generate it initially

################



def help_string():
    return '''
Help:

-------New issue-------
new title_str [body_str [label_nums_list]] 

 - substitute 'nd' for 'new' for new deferred action
 - 'n' can be used for 'new'

Example:
n 'Organize closet' '' '3,6' # Creates task with no body and two labels

-------Other commands-------
        ('exit','x','quit','q'):
            # Ends loop execution, exits program
            break 
        
        ('help', 'h'):
            print(help_string())
        
        ('new', 'n'):
            create_issue(cmd[1:], 'action') # cmd[1:] is: title [, body [, label_numbers_list]]
        
        'nd':
            create_issue(cmd[1:], 'defer') # cmd[1:] is: title [, body [, label_numbers_list]]
        
        'label':
            create_label(cmd[1])

        'll':
            list_labels()

        'li':
            list_issues('open')

        'lic':
            list_issues('closed')

        'wipe':
            wipe_and_close_issue(cmd[1])

        'close':
            if len(cmd) > 2:
                close_issue(cmd[1], cmd[2])
            else:
                close_issue(cmd[1])
'''

def create_new_issue_label_list(label_num_text):
    import re
    try:
        label_num_list = map(int, re.split(' *, *', label_num_text))
    except:
        raise ValueError('Error: Label number list must be comma-separated: "%s"' % label_num_text)

    new_issue_label_list = []
    for num in label_num_list:
        if( len(labels_list) > num ):
            new_issue_label_list.append(labels_list[num])
        else:
            print('Label number %d not found in label list' % num)
    return new_issue_label_list

def get_milestone_num(milestone_text):
    # Todo - revise this to not be hard-coded
    if milestone_text in ('action','actionable'):
        return (1, 'ransage')
    elif milestone_text in ('defer','deferred'):
        return (2, '')
    else:
        return None

def display_formatted_issue(issue):
    print('%s %s (%s %d, %s)' % 
          (issue.title, 
           str(map(str,issue.labels)),
           issue.repository[1], 
           issue.number, 
           issue.milestone,
           )
          )

def list_issues(requested_state=None):
    if not requested_state in ('open','closed'):
        raise ValueException("Function only allows 'open' or 'closed'")
    # List in the order of active repositories
    for rep_path in settings['active_repos']:
        print("=====================%s====================="%rep_path)
        user, rep_name = rep_path.split('/')
        rep = gh.repository(user, rep_name)
        for issue in rep.iter_issues(assignee=username,
                                     state=requested_state):
            display_formatted_issue(issue)

def create_body_string(text_to_insert):
    body_string_preface = '''WARNING: python auto-generated this text and it is likely to get edited and/or deleted.
Use comments if you want to append information to this issue.
[debugging] [auto-gen]

--------------------

'''
    return (body_string_preface + text_to_insert)

def wipe_and_close_issue(issue_num):
    issue = repo.issue(issue_num)
    print('This will wipe the following issue (DESTRUCTIVE)')
    display_formatted_issue(issue)
    if query_yes_no('Do you want to proceed?',default='no'):
        issue.edit(title='DELETED',
                   body='',
                   assignee='',
                   milestone=0, # expects 1-based int; 0 to remove the milestone
                   labels=[]) # expects list
        close_issue(issue_num, 'Issue wiped/deleted')
    else:
        print('Wipe aborted')

def close_issue(issue_num, reason_text=''):
    issue = repo.issue(issue_num)
    close_preface = '\n\n--------------------\n[Item closed by python script...]\n\n'
    close_message = close_preface + reason_text
    try:
        new_body_text = issue.body + close_message
        if issue.edit(body=new_body_text):
            return issue.close()
        else:
            print('Failed to edit so not closing issue: "%s"' % str(issue))
            return False
    except:
        print('Caught exception trying to close issue: "%s"' % str(issue))
        return None

def create_issue(arg_list, milestone_text='action'):
    if len(arg_list) == 0:
        print('No title provided - not doing anything')
        return False

    title_string = arg_list[0]
    if( len(arg_list) < 1 ):
        body_text = ''
    else:
        body_text = create_body_string(arg_list[1])

    if( len(arg_list) < 2 ):
        labels_list = []
    else:
        try:
            labels_list = create_new_issue_label_list(arg_list[2])
        except ValueError as ex:
            print(ex.message)
            return
  
    try:
        new_issue = repo.create_issue(title=title_string)
        if debug_on:
            print('No exception, returned: %s' % str(new_issue))
    except:
        new_issue = None
        if debug_on:
            print('Exception for "%s" - setting to None ' % title_string)
    
    milestone_num, assignee_name = get_milestone_num(milestone_text)


    if(new_issue):
        success = new_issue.edit(body=body_text,
                                 assignee=assignee_name,
                                 milestone=milestone_num,
                                 labels=labels_list)
        if(success):
            print('Success')
        else:
            print('Created following issue with title only:\n  "%s"' % title_string)
    else:
        print('!!! Failed to create issue %s !!!' % title_string)

def list_labels():
    print('--- Labels with numbers ---')
    for index in range(0,len(labels_list)):
        print('%d: %s'%(index, labels_list[index]))

def create_label(new_label_name, color_string = '#bbbb00'):
    if query_yes_no('This will create label, %s - are you sure you want to continue?' 
                    % new_label_name,
                    default='no'):
        try:
            new_label = repo.create_label(new_label_name, color_string)
            if new_label:
                print('Successfully created label: %s'%str(new_label))
                generate_labels_list()
                return True
        except:
            print('Caught exception in create_label')
            pass
        print('Did not create label')
        return False
    else:
        print('Not attempting to create label due to user response')

if __name__ == "__main__":
    import readline
    import shlex

    print('Enter a command to do something, e.g. `create name price`.')
    print('To get help, enter `help`.')

    list_labels()
    while True:
        print('\n==========================================')
        print(  '==========================================')
        print('User %s and Active project/repo: %s' % (username, repo))

        cmd = shlex.split(raw_input('> '),True) # True enables comments

        if len(cmd) == 0:
            pass

        elif cmd[0] in ('exit','x','quit','q'):
            # Ends loop execution, exits program
            break 
        
        elif cmd[0] in ('help', 'h'):
            print(help_string())
        
        elif cmd[0] in ('new', 'n'):
            create_issue(cmd[1:], 'action') # cmd[1:] is: title [, body [, label_numbers_list]]
        
        elif cmd[0]=='nd':
            create_issue(cmd[1:], 'defer') # cmd[1:] is: title [, body [, label_numbers_list]]
        
        elif cmd[0]=='label':
            create_label(cmd[1])

        elif cmd[0]=='ll':
            list_labels()

        elif cmd[0]=='li':
            list_issues('open')

        elif cmd[0]=='lic':
            list_issues('closed')

        elif cmd[0]=='wipe':
            wipe_and_close_issue(cmd[1])

        elif cmd[0]=='close':
            if len(cmd) > 2:
                close_issue(cmd[1], cmd[2])
            else:
                close_issue(cmd[1])

        # TODO - create better method for generating doc from app logic or vice versa 
        #             such as docparse plus iterative calls to app from interactive
        # TODO - add option for creating incubate
        
        # ...
        
        else:
            print('Unknown command: {}'.format(cmd))
    print('Done')

print('End of file')

