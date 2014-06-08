#! ./venv/bin/python

##############
# TEMP/DEBUG
debug_on = True
##############

import shelve
import os.path

import json

with open('settings.json') as json_file:
    s = json.load(json_file)

shelf_filename = os.path.expanduser(s['config_filename'])

shelf = shelve.open(shelf_filename)

try:
    if shelf.has_key('app_running') and shelf['app_running']:
        shelf['app_running'] = False
        shelf.close()
    else:
        print 'No need to unlock shelf; doing nothing'
except:
    print 'Failed to unlock shelf'
