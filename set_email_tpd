from pymongo import MongoClient
from settings import NSN
import re

mlab_uri = "mongodb://af:gehrig10@ds059702.mlab.com:59702/tpd"

client = MongoClient(mlab_uri)

db = client.tpd
store = int(NSN)
w, h = 2, 10
email_list = [[" " for x in range(w)] for y in range(h)]

for i in range(2):
    level = i+1
    get_emails = db.email.find({"store": store, "level": level})
    for document in get_emails:
        #print document
        email_list[i] = document["email_list"]

l1match = re.findall(r'[\w\.-]+@[\w\.-]+', email_list[0])
l2match = re.findall(r'[\w\.-]+@[\w\.-]+', email_list[1])

with open(r'/home/pi/TPD/Emails/emaillevel1.txt', 'w+') as thefile:
    for item in l1match:
        thefile.write("%s\n" % item)

with open(r'/home/pi/TPD/Emails/emaillevel2.txt', 'w+') as thefile:
    for item in l2match:
        thefile.write("%s\n" % item)
