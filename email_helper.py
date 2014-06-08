#! ./venv/bin/python

import imaplib
import json
import re
import time
import email
#from email.message import Message
from email.mime.text import MIMEText

debug_on = False

with open('settings.json') as json_file:
    s = json.load(json_file)

def getFoldersList(obj):
    t,folder_list = obj.list()
    
    folders_list = []
    for i in range(0,len(folder_list)):
        results = re.findall( (re.escape(s['folder_prefix']) +
                               '''[^'"]*'''),
                              folder_list[i])
        if len(results):
            folder_name = results[0].replace(s['folder_prefix'],'')
            folders_list.append(folder_name)
        if len(results) > 1:
            print 'WARNING: disregarding results after first...'
            print results[1:]
    return folders_list

def createMessage(folder, subject_text, body_text):
    if len(body_text) == 0:
        body_text = ' '
    if debug_on:
        print "Folder: %s" % folder
        print "Subject: %s" % subject_text
        print "-----Body----- \n%s" % body_text

    obj = imaplib.IMAP4_SSL(s['secure_mail_server'],'993')
    obj.login(s['username'],s['password'])

    if len(folder) == 0:
        full_name = s['folder_prefix'][:-1] # Chop dot from INBOX.
    elif folder in getFoldersList(obj):
        full_name = s['folder_prefix'] + folder
        obj.select(full_name)
        print 'Selected folder: %s' % full_name
    else:
        raise ValueError('Error: folder name (%s) not in folder list' % folder)
    flags = ''

    msg = MIMEText(body_text)
    msg['Subject'] = subject_text
    msg['From'] = s['sender']
    msg['To'] = s['address']

    obj.append(full_name, 
               flags,
               imaplib.Time2Internaldate(time.time()),
               msg.as_string())

def issue_on_server(issue_id):
    obj = imaplib.IMAP4_SSL(s['secure_mail_server'],'993')
    obj.login(s['username'],s['password'])
    obj.select()
    p,res = obj.search(None, 'BODY', issue_id)
    return len(res[0])>0

def getDataFromEmail():
    prev = time.time()
    
    obj = imaplib.IMAP4_SSL(s['secure_mail_server'],'993')
    obj.login(s['username'],s['password'])
    obj.select()

    print obj.list

    searchStr = '['
    results = obj.search(None,'SUBJECT',searchStr)
    if results[0] == 'OK':
        msg = obj.fetch(results[1][0],'(UID BODY[TEXT])')
        if msg[0] == 'OK':
            #import pdb; pdb.set_trace()
            msgBody = msg[1][0][1]
            startIndex = msgBody.find('Turn ')
            endIndex = msgBody.find('--------Reply To Instructions------')
            outFile.write(msgBody[startIndex:endIndex])
            print 'SUCCESS'
        else:
            print 'FAILURE'
            #return (obj,results,msg)
    else:
        print 'FAILURE'
        #return (obj,results)

    # for .close(): Due to buffering, the string may not actually show
    #  up in the file until the flush() or close() method is called.
    outFile.close()

    print 'elapsed time = ' + str(time.time()-prev)
        

def sendEmail(message, 
              subject='System generated email from gsd',
              recipient = s['address'] # Default to self
              ):
    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules we'll need
    from email.mime.text import MIMEText

    mime_message = MIMEText(message)


    me = s['address']

    mime_message['Subject'] = subject
    mime_message['From'] = me
    mime_message['To'] = recipient

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL(s['secure_mail_server'],'465')
    s.login(s['username'],s['password'])

    s.sendmail(me, [recipient], mime_message.as_string())

    s.quit()

if __name__ == '__main__':
    import sys
    import getpass

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = 'ransage'

    print 'About to create message in folder Test'
    createMessage('Test','Test message subject','test message body\nwith multiple\lines')

    print 'About to create message in inbox'
    createMessage('','Inbox test message','test inbox message body\nwith multiple\lines')

    print '\nThis should raise...'
    try:
        createMessage('aoeu',[],[])
    except ValueError as e:
        print 'CAUGHT!  ',
        print e

    print '------\nDone!'
