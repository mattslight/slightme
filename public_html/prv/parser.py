#!/usr/bin/env python
import json
import urllib
import base64
import requests
from urllib.request import Request, urlopen
from urllib.error import URLError
from pprint import pprint

#Set up API and REQUEST strings
API_KEY = "231506b67b2f31242d542c0de6287cd3"
PASSWORD = "83353183b0af13c806a3dffee3f28f65"
REQ_URL = "https://prosfx.myshopify.com"
REQ_GET_ORDER = "/admin/orders.json"
REQ_PUT_ORDER =  "/admin/orders/%s.json" # %s should be order id
TAG = "Quote" #tag to check for and add

#Auth handshake
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, REQ_URL, API_KEY, PASSWORD)
auth_handler = urllib.request.HTTPBasicAuthHandler(passman)

#Prepare the URL opener
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)

#Get the urlopen response
orders_response = urlopen(REQ_URL + REQ_GET_ORDER)
orders_json = orders_response.read().decode('utf-8') #convert response from bytes to str
orders_data = json.loads(orders_json) #convert JSON str to python dict

#iterate orders over dict obj
for order in orders_data['orders']:
    if order['gateway'] == "Quotation Only": #check if payment gateway matches 'Quotation Only'
        if(TAG not in order['tags']):
            if (order['tags']):
                TAGS = order['tags'] + (", %s" % TAG)
            else:
                TAGS = TAG
            
            PAYLOAD = '{"order": {"id": "%s", "tags": "%s"}}' % (order['id'], TAGS)
            
            r_url=(REQ_URL + (REQ_PUT_ORDER % order['id']))
            r_headers = {'Content-Type': 'application/json'}
            
            r = requests.put(url=r_url, data=PAYLOAD, auth=(API_KEY, PASSWORD), headers=r_headers)
            print("Status Code: %s" % r.status_code)
            
