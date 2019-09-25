#!/usr/bin/env python
import json
import re
import urllib

def getAirtimeJson(server, postfix):
    try:
        response = urllib.urlopen('https://{0}/{1}'.format(server, postfix))
    except urllib.URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach the server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Code: ', e.code)
        exit()

    str_response = response.read().decode('cp1252')
    return str_response

def parseAirtimeJson(str_response):
    try:
        jsonObj = json.loads(str_response)
    except ValueError as e:
        print('Invalid JSON: ', str_response)
        exit()

    return jsonObj

server = "airtime.herhq.org"
postfix = "api/live-info"

jsonStr = getAirtimeJson(server, postfix)

obj = parseAirtimeJson(jsonStr)

showName = "Unknown"
if 'currentShow' in obj:
    if (len(obj['currentShow']) > 0):
        if 'name' in obj['currentShow'][0]:
            showName = re.sub("[^a-zA-Z0-9-]", "", obj["currentShow"][0]["name"].strip())

print showName
