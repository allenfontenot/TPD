#!/usr/bin/env python

import sys
from settings import *
import datetime
from sendmail import *
import os
import logging
import socket

logging.basicConfig(filename='logs/debug2.log', level=logging.DEBUG)

logging.debug(str(datetime.datetime.now()) + ' Running Check started')

# PID for TPD is logged in pid.txt, checks if running and restarts if not
with open('logs/pid.txt', 'r') as qq:
    qqq = qq.readline()
pidpath = "/proc/" + str(qqq)

now = datetime.datetime.now()
msg = str(now) + ' TPD not updating restarting now'
msg2 = str(now) + ' TPD is working'

if os.path.exists(pidpath) is False:
    try:
        sendstoppedmail(NSN, 5)
    except socket.gaierror:
        logging.debug(str(now) + ' email failed')
    logging.debug(msg)
    os.system("sudo shutdown -r now")
else:
    logging.debug(msg2)
