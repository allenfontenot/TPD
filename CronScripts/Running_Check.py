#!/usr/bin/env python

from settings import *
import datetime
from sendmail import *
import os
import logging

logging.basicConfig(filename='~/TPD/logs/debug.log', level=logging.DEBUG)

logging.debug(str(datetime.datetime.now()) + ' Running Check started')

with open('/logs/debug.log', 'r') as qq:
    qqq = qq.readlines()

lastline = len(qqq) - 1

a = qqq[lastline]
print a
FMT = '%Y-%m-%d %H:%M:%S.%f'

b = a.split()
b2 = str(b[0] + ' ' + b[1])

print b2

c = datetime.datetime.strptime(b2, FMT)

d = datetime.datetime.now()

e = datetime.timedelta(minutes=5)

print c

print d

print d - c

now = datetime.datetime.now()
msg = str(now) + ' TPD not updating restarting now'
msg2 = str(now) + ' TPD is working'

if d - c > e:
    sendstoppedmail(NSN, 5)
    logging.debug(msg)
    os.system("sudo shutdown -r now")
else:
    logging.debug(msg2)
