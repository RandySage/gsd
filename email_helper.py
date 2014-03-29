import json
with open('settings.json') as json_file:
    settings = json.load(json_file)

def getDataFromEmail():

    import imaplib
    import re

    from time import time
    prev = time()
    
    obj = imaplib.IMAP4_SSL(settings['secure_mail_server'],'993')
    obj.login(settings['username'],settings['password'])
    obj.select()

    print obj.list

    searchStr = '['
    results = obj.search(None,'SUBJECT',searchStr)
    if results[0] == 'OK':
        msg = obj.fetch(results[1][0],"(UID BODY[TEXT])")
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

    print 'elapsed time = ' + str(time()-prev)
        

def sendEmail(message, 
              subject='System generated email from gsd',
              recipient = settings['address'] # Default to self
              ):
    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules we'll need
    from email.mime.text import MIMEText

    mime_message = MIMEText(message)


    me = settings['address']

    mime_message['Subject'] = subject
    mime_message['From'] = me
    mime_message['To'] = recipient

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP_SSL(settings['secure_mail_server'],'465')
    s.login(settings['username'],settings['password'])

    s.sendmail(me, [recipient], mime_message.as_string())

    s.quit()

