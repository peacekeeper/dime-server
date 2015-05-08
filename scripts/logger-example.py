#!/usr/bin/env python3

import requests
import sys
import socket
import time
import json

#------------------------------------------------------------------------------

server_url = 'http://localhost:8080/api'
server_username = 'testuser'
server_password = 'testuser123'

#------------------------------------------------------------------------------

r = requests.post(server_url + '/ping')

if r.status_code != requests.codes.ok:
    print('No connection to DiMe server!')
    sys.exit(1)


# Set all the standard event fields
payload = {
    'actor':    'logger-example.py',
    'origin':   socket.gethostbyaddr(socket.gethostname())[0],
    'type':     'http://www.hiit.fi/ontologies/dime/#ExampleSearchEvent',
    'start':    time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime()),
    'duration': 0,
}

payload['query'] = "dummy search"

requests.post(server_url + '/data/searchevent',
                         data=json.dumps(payload),
                         headers={'content-type': 'application/json'},
                         auth=(server_username, server_password),
                         timeout=10)
