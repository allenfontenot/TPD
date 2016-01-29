#import plotly
#print plotly.__version__ # version >1.9.4 required
#from plotly.graph_objs import Scatter, Layout

NSN = 10841

import json,httplib,urllib
import datetime
from datetime import datetime

connection = httplib.HTTPSConnection('api.parse.com', 443)

#Pulls from parse entries that match NSN
params = urllib.urlencode({
    "where":json.dumps({
     "store": NSN
    }),
    "order":"createdAt",
    "keys":"average,violation,firstTravelPath,lastTravelPath,createdAt"})

connection.connect()
connection.request('GET', '/1/classes/yesterdayNumbers', '', {
       "X-Parse-Application-Id": "BupCLnOBroEGuXa9qkAWebNSzT0o18MTUQeXNJXO",
       "X-Parse-REST-API-Key": "oSYBMvF2ET9RvyWhxnIpYa27rObd4XATJoh9zueh"
     })
result = json.loads(connection.getresponse().read())
a = len(result['results'])
print a
print result

#Arrays for values pulled from parse
avgList = []
vioList = []
firstTravelList = []
lastTravelList = []
createdAtList = []

#Pull values out of json results
for i in range(0, a):
    avg = result['results'][i]['average']
    violation = result['results'][i]['violation']
    firstTravel = result['results'][i]['firstTravelPath']
    lastTravel  = result['results'][i]['lastTravelPath']
    createdAt = result['results'][i]['createdAt']

    avgList.append(avg) 
    vioList.append(violation)
    firstTravelList.append(firstTravel)
    lastTravelList.append(lastTravel)
    createdAtList.append(createdAt)

print 'avglist contains'
for i in avgList: print i
for i in vioList: print i

for n,i in enumerate(firstTravelList): 
    q = datetime.strptime(i, "%Y-%m-%j %H:%M:%S.%f")
    lastTravelList(n) = str(q.time())

for n,i in enumerate(lastTravelList):
    q = datetime.strptime(i, "%Y-%m-%j %H:%M:%S.%f")
    lastTravelList[n] = str(q.time())

for n,i in enumerate(createdAtList):
    q = datetime.strptime(i, "%Y-%m-%jT%H:%M:%S.%fZ")
    createdAtList[n] = q.day

print "first path of the day"
print firstTravelList
print "last path of the day"
print lastTravelList
print 'days'
print createdAtList

'''plotly.offline.plot({
"data": [
    Scatter(x=[1,2,3,4], y=[4,1,3,8])
],
"layout": Layout(
    title="hello world"
)
})
'''
