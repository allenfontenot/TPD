#!/usr/bin/env python

from background import *
import json
import httplib
#from settings import NSN


NSN = 10841

###GET VALUES FROM LOG###
violation = 0
average = 0
firstTravelPath = ""
lastTravelPath = ""

##get average##
zd1 = []
bb = []
with open('logs/travellog.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        a = int(row[2])
        b = row[0]
        zd1.append(a)
        bb.append(b)

zd2 = filter(lambda aa: aa != 0, zd1)  # takes out the zeroes
average = sum(zd2) / len(zd2)
lastTravelPath = bb[(len(bb)-1)]
firstTravelPath = bb[7]
###############

##get violation
zd1 = []
with open('logs/violations.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        violation += 1
###############

###SEND EVERYTHING TO PARSE###

connection = httplib.HTTPSConnection('api.parse.com', 443)

#create new objects instead of updating
try:
    connection.connect()
    connection.request('POST', '/1/classes/yesterdayNumbers', json.dumps({
           "store": NSN,
           "violation": violation,
           "average": average,
           "firstTravelPath": firstTravelPath,
           "lastTravelPath": lastTravelPath
         }), {
           "X-Parse-Application-Id": "BupCLnOBroEGuXa9qkAWebNSzT0o18MTUQeXNJXO",
           "X-Parse-REST-API-Key": "oSYBMvF2ET9RvyWhxnIpYa27rObd4XATJoh9zueh",
           "Content-Type": "application/json"
         })
    results = json.loads(connection.getresponse().read())
    logging.debug(results)

except Exception:
    print "Connection Failed"
    logging.debug("Parse Connection Failed")
    pass
