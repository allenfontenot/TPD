#!/usr/bin/env python

import pygame
import pygame.gfxdraw
#import RPi.GPIO as GPIO
from datetime import timedelta
from background import *
from pygame.locals import *
from sendmail import *
import socket
import json
import httplib

connection = httplib.HTTPSConnection('api.parse.com', 443)

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
logging.basicConfig(filename='logs/debug.log', level=logging.DEBUG)

# Initialize GPIO
#GPIO.setmode(GPIO.BCM)
#gp = [2, 3, 4, 14, 15, 18]  # Pins to Initialize
#for i in gp:
#    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#    logging.debug(str(timenow()) + ' GPIO ' + str(i) + ' setup')#

# interrupt pin setup
#cb = [interrupt1, interrupt2, interrupt3, interrupt4, interrupt5, interrupt6]  # list of interrupt functions
#for i, j in zip(gp, cb):

#        GPIO.add_event_detect(i, GPIO.FALLING, callback=j, bouncetime=300)

# Draws initial UI
drawitall()
logging.debug(str(timenow()) + " Background Drawn")

# store pid to file
writepidfile()

# mail timers for not spamming notifications initialized for first pass
tm = tm2 = datetime(1999, 1, 1, 0, 0, 0, 0)
lm = lm2 = datetime(1999, 1, 1, 0, 0, 0, 0)
onlineFirstRun = True
offlineFirstRun = True
fromOffline = False

while True:  # Main Loop contains 1 loop for offline and 1 loop for online

    while datetime.now().time() > offlinetime or datetime.now().time() < onlinetime:
        timecomp()
        if offlineFirstRun:
            logging.debug(str(timenow()) + '  offline')
            try:
                sendmail("offline", 0, 0, NSN, 5)
            except socket.gaierror:
                logging.debug(str(timenow()) + ' email failed')
            print str(datetime.now()) + " offline"
            for i in range(1, 4):
                circles(i, red)
                travelList(i)
                number(i, "offline")
                complications(i)
                comptext(i, ct[i - 1])
                compnumber(i, "offline")
            offlineFirstRun = False

        lcd.blit(background, (0, 0))
        pygame.display.flip()
        onlineFirstRun = True
        fromOffline = True
        exit()

# Not Offline
    # update complications
    timecomp()
    avgcomp()
    viocomp()
    pygame.display.flip()

    if onlineFirstRun:  # online notification first time through

        logging.debug(str(timenow()) + ' online')
        try:
            sendmail("online", 0, 0, NSN, 5)
        except socket.gaierror:
            logging.debug(str(timenow()) + ' email failed')

        onlineFirstRun = False

    if fromOffline:  # if we came from offline to online then reset all timers
        outputFile = open('logs/travellog.csv', 'a')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([timenow(), zone1, 60, NSN])
        outputWriter.writerow([timenow(), zone2, 60, NSN])
        outputWriter.writerow([timenow(), zone3, 60, NSN])
        outputFile.close()
        fromOffline = False

    # subtract stored time from current
    for i in range(3):
        j = i + 1
        lastTime[i] = findlasttime(j)
        q = datetime.strptime(lastTime[i], FMT)
        r = timenow() - q
        e = int(r.total_seconds() / 60)
        if e != ltsec[i]:  # if minutes have changed update screen
            logging.debug(str(timenow()) + ' changing zone' + str(j) + ' to ' + str(e))
            ltsec[i] = e
            if e < yellowLimit:
                color = green
            elif redLimit > e >= yellowLimit:
                color = yellow
            else:
                color = red
            circles(j, color)
            travelList(j)
            number(j, e)

            lcd.blit(background, (0, 0))
            pygame.display.flip()
            # send updated numbers to parse
            objectid = ""
            if i == 0:
                objectid = z1ids[NSNlist.index(NSN)]
            elif i == 1:
                objectid = z2ids[NSNlist.index(NSN)]
            elif i == 2:
                objectid = z3ids[NSNlist.index(NSN)]
            
            objectstring = '/1/classes/lasttravel/' + str(objectid)
            try:
                connection.connect()
                connection.request('PUT', objectstring,
                                   json.dumps({"minutes": e}),
                                   {"X-Parse-Application-Id": "BupCLnOBroEGuXa9qkAWebNSzT0o18MTUQeXNJXO",
                                    "X-Parse-REST-API-Key": "oSYBMvF2ET9RvyWhxnIpYa27rObd4XATJoh9zueh",
                                    "Content-Type": "application/json"})
                result = json.loads(connection.getresponse().read())
                logging.debug(result)
            except Exception:
                logging.debug("Parse Connection Failed")
                pass

    # Check for violations
    if max(ltsec) >= mailtimeLevel1:  # only checks the highest value...doesn't matter which is higher
        lvl = 1
        tm = timenow()  # this mail is now

        if lm + timedelta(0, tba) < tm:
            try:
                sendmail(ltsec[0], ltsec[1], ltsec[2], NSN, lvl)
            except socket.gaierror:
                logging.debug(str(timenow()) + ' email failed')
            print "level 1 email sent at " + str(timenow())
            logging.debug(str(timenow()) + " level 1 email sent")
            lm = tm
            Violation(timenow(), 'zone', lvl, max(lastTime))

    if max(ltsec) >= mailtimeLevel2:
        lvl = 2
        tm2 = timenow()  # this mail is now

        if lm2 + timedelta(0, tba) < tm:  # check for last email sent and don't send if within tba
            try:
                sendmail(ltsec[0], ltsec[1], ltsec[2], NSN, lvl)
            except socket.gaierror:
                logging.debug(str(timenow()) + ' email failed')
            print "level 2 email sent at " + str(timenow())
            logging.debug(str(timenow()) + " level 2 email sent")
            lm2 = tm2
            Violation(timenow(), 'zone', lvl, max(lastTime))

    offlineFirstRun = True  # to send the offline notifications when it goes back to that loop
    exit()
