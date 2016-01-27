#!/usr/bin/env python

from background import *
import json
import httplib
#from settings import NSN
from settings import NSNlist

NSN = '10841'

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
        print row
        a = int(row[2])
        print 'a=' + str(a)
        b = row[0]
        print 'b=' + str(b)
        zd1.append(a)
        bb.append(b)

        print zd1
        print bb
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

weeklyObjectIdList = ["H4nYULUo31","griFoSEZDk","EjmReTVEvl","8zxVdPEa8I","MWZaLsi24R","mHW0jhUSEV","fKKKGVjwUS","plP4YQWBns","qvsOip2hwb","FXfxglBaLJ"]
yesterdayObjectIdList = ["5i1tLcJEZH","E7dWjWHJHs","S7f2OaNzEZ","LlXnnbSj6L","OuLXZ6mx2e","3KlKMMfH4f","23frTQgJLg","8bCL5w9QYM","2UPvz6P78c","JPfeqFuG2Z"]
monthlyObjectIdList = ["FRhJlsyEHx","TPcC63O2T8","LIa8VtuiNr","TaSlFH90nJ","FU4HTADmh7","YyXrEaWqj2","R6gU8qBtdm","Fp5j3faFQe","Nu5LbTejmM","XosQXKIoCS"]

weeklyObjectId = weeklyObjectIdList[NSNlist.index(NSN)]
yesterdayObjectId = yesterdayObjectIdList[NSNlist.index(NSN)]
monthlyObjectId = monthlyObjectIdList[NSNlist.index(NSN)]


weeklyObjectString = '/1/classes/weeklyNumbers/' + str(weeklyObjectId)
yesterdayObjectString = '/1/classes/yesterdayNumbers/' + str(yesterdayObjectId)
mothlyObjectString = '/1/classes/monthlyNumbers/' + str(monthlyObjectId)
try:
    connection.connect()
    connection.request('PUT', yesterdayObjectString,
                       json.dumps({"violation": violation}),
                       {"X-Parse-Application-Id": "BupCLnOBroEGuXa9qkAWebNSzT0o18MTUQeXNJXO",
                        "X-Parse-REST-API-Key": "oSYBMvF2ET9RvyWhxnIpYa27rObd4XATJoh9zueh",
                        "Content-Type": "application/json"})
    result = json.loads(connection.getresponse().read())
    logging.debug(result)
    connection.request('PUT', yesterdayObjectString,
                       json.dumps({"average": average}),
                       {"X-Parse-Application-Id": "BupCLnOBroEGuXa9qkAWebNSzT0o18MTUQeXNJXO",
                        "X-Parse-REST-API-Key": "oSYBMvF2ET9RvyWhxnIpYa27rObd4XATJoh9zueh",
                        "Content-Type": "application/json"})
    result = json.loads(connection.getresponse().read())
    logging.debug(result)

    connection.request('PUT', yesterdayObjectString,
                       json.dumps({"lastTravelPath": lastTravelPath}),
                       {"X-Parse-Application-Id": "BupCLnOBroEGuXa9qkAWebNSzT0o18MTUQeXNJXO",
                        "X-Parse-REST-API-Key": "oSYBMvF2ET9RvyWhxnIpYa27rObd4XATJoh9zueh",
                        "Content-Type": "application/json"})
    result = json.loads(connection.getresponse().read())
    logging.debug(result)
    connection.request('PUT', yesterdayObjectString,
                       json.dumps({"firstTravelPath": firstTravelPath}),
                       {"X-Parse-Application-Id": "BupCLnOBroEGuXa9qkAWebNSzT0o18MTUQeXNJXO",
                        "X-Parse-REST-API-Key": "oSYBMvF2ET9RvyWhxnIpYa27rObd4XATJoh9zueh",
                        "Content-Type": "application/json"})
    result = json.loads(connection.getresponse().read())
    logging.debug(result)

except Exception:
    logging.debug("Parse Connection Failed")
    pass

