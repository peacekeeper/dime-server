#!/usr/bin/env python

import os
import sys
import mailbox
import requests
import argparse
import time
import rfc822
import pprint

from dlog_globals import config
import dlog_conf as conf
import dlog_common as common

#------------------------------------------------------------------------------

def create_payload(message, i, tag_category, tag_frequency):

    print "---###---###---###---###---###---###---###---###---###---###---"
    print
    print '%d: %s "%s" from %s' % (i, message['Message-ID'], message['subject'], message['from'])
    print
    
    if message['Message-ID'] is None:
        print 'Error: No "Message-ID" found on, skipping'
        return None
    
    if message['date'] is None:
        print 'Error: No "date" found on %s, skipping' % message['Message-ID']
        return None
        
    dt = 1000*int(rfc822.mktime_tz(rfc822.parsedate_tz(message['date'])))
    
    payload = {
        '@type':  'MessageEvent',
        'actor':    'mbox2dime.py',
        'origin':   config['hostname'],
        'type':     'http://www.hiit.fi/ontologies/dime/#EmailEvent',
        'start':    dt,
        'duration': 0}
    
    targettedResource = {
        '@type':      'Message',
        'uri': 'Message-ID:'+message['Message-ID'],
        'type': 'http://www.semanticdesktop.org/ontologies/2007/03/22/nmo/#Email',
        'isStoredAs': 'http://www.semanticdesktop.org/ontologies/2007/03/22/nmo/#MailboxDataObject',
        'date': message['date'],
        'subject': message['subject'],
        'fromString': message['from'],
        'toString': message['to'],
        'ccString': message['cc'],
        'tags' : ['enron_category='+tag_category, 'enron_frequency='+tag_frequency]
        #'attachments': [],
        #'rawMessage': '' # the full raw message here...
    }

    targettedResource['id'] = common.to_json_sha1(targettedResource)
    payload['targettedResource'] = {}
    payload['targettedResource']['id'] = targettedResource['id']
    payload['id'] = common.to_json_sha1(payload)

    msgpayload = message.get_payload()
    msgtext = ''
    while isinstance(msgpayload, list): 
        msgpayload = msgpayload[0].get_payload()

    if isinstance(msgpayload, str):
        msgtext = msgpayload
            
    targettedResource['plainTextContent'] = msgtext    

    payload['targettedResource'] = targettedResource.copy()

    return common.json_dumps(payload, indent=2)

#------------------------------------------------------------------------------

if __name__ == "__main__":

    print "Starting the enron2dime.py logger on " + time.strftime("%c")

    parser = argparse.ArgumentParser(description='Sends Enron (enron_with_categories) emails to DiMe.')

    parser.add_argument('emailfile', metavar='FILE',
                        help='list of Enron emails to be processed')
    parser.add_argument('--dryrun', action='store_true',
                        help='do not actually send anything')
    parser.add_argument('--limit', metavar='N', action='store', type=int,
                        default=0, help='process only N first emails')

    args = parser.parse_args()

    cwd = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    conf.configure(inifile="enron.ini")
    os.chdir(cwd)

    pingstring = "Pinging DiMe server at location: " + config['server_url'] + " : "
    if common.ping_server():
        print pingstring + "OK"
    else:
        print pingstring + "FAILED"
        if not args.dryrun:
            print 'Ping failed and "--dryrun" not set, exiting'
            sys.exit()

    i=1
    with open(args.emailfile) as f:
        for line in f:
            line = line.rstrip()
            parts = line.split(" ")
            print "Processing [{}] [{}] [{}] [{}]".format(line, *parts)
            mbox = mailbox.mbox(parts[0])
            if len(mbox) != 1:
                print "ERROR: Multiple emails found in", parts[0]
                break
            for message in mbox:
                json_payload = create_payload(message, i, parts[1], parts[2])
                if json_payload is None:
                    continue
                print "PAYLOAD:\n" + json_payload

                if not args.dryrun:
                    common.post_payload(json_payload, "messageevent")

            if args.limit>0 and i >= args.limit:
                break
            i=i+1

    print "Processed %d entries" % i
    
#------------------------------------------------------------------------------
