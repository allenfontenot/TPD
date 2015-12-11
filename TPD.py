#!/usr/bin/env python

import pygame
import pygame.gfxdraw
import RPi.GPIO as GPIO
from datetime import timedelta
from background import *
from pygame.locals import *
from sendmail import *
import socket

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
logging.basicConfig(filename='logs/debug.log', level=logging.DEBUG)

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
gp = [2, 3, 4, 14, 15, 18]  # Pins to Initialize
for i in gp:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    logging.debug(str(timenow()) + ' GPIO ' + str(i) + ' setup')

# interrupt pin setup
cb = [interrupt1, interrupt2, interrupt3, interrupt4, interrupt5, interrupt6]  # list of interrupt functions
for i, j in zip(gp, cb):

        GPIO.add_event_detect(i, GPIO.FALLING, callback=j, bouncetime=300)

# Draws initial UI
drawitall()
logging.debug(str(timenow()) + " Background Drawn")

# store pid to file
writepidfile()

# mail timers for not spamming notifications initialized for first pass
tm = tm2 = datetime(1999, 1, 1, 0, 0, 0, 0)
lm = lm2 = datetime(1999, 1, 1, 0, 0, 0, 0)
logcount = 0
logcount2 = 0

while True:  # Main Loop contains 1 loop for offline and 1 loop for online
    #logging.debug(str(timenow()) + ' main loop started')
    while datetime.now().time() > offlinetime or datetime.now().time() < onlinetime:
        timecomp()
        if logcount2 == 0:
            logging.debug(str(timenow()) + '  offline')
            try:
                sendmail("offline", 0, 0, NSN, 5)
            except socket.gaierror:
                logging.debug(str(timenow()) + ' email failed')
            print str(datetime.now()) + " offline"
            for i in range(1, 4):
                circles(i, red)
                footers(i)
                number(i, "offline")
                complications(i)
                comptext(i, ct[i - 1])
                compnumber(i, "offline")
            logcount2 = 1

        lcd.blit(background, (0, 0))
        pygame.display.flip()
        logcount = 0  # so that online loggin and email only sent if offline first
        exit()

# Not Offline
    # draw 3 complications
    timecomp()
    avgcomp()
    viocomp()
    pygame.display.flip()

    if logcount == 0:  # online notification first time through
        logging.debug(str(timenow()) + ' online')
        try:
            sendmail("online", 0, 0, NSN, 5)
        except socket.gaierror:
            logging.debug(str(timenow()) + ' email failed')

        logcount = 1

    # subtract stored time from current
    for i in range(3):
        j = i + 1
        lastTime[i] = findlasttime(j)
        q = datetime.strptime(lastTime[i], FMT)
        r = timenow() - q
        e = int(r.total_seconds() / 60)
        #print 'e = ' + str(e)
        #print 'lt = ' + str(ltsec[i])
        if e != ltsec[i]:
            logging.debug(str(timenow()) + ' changing zone' + str(j) + ' to ' + str(e))
        ltsec[i] = e
        if e < yellowLimit:
            color = green
        elif redLimit > e >= yellowLimit:
            color = yellow
        else:
            color = red
        circles(j, color)
        footers(j)
        number(j, e)

    lcd.blit(background, (0, 0))
    pygame.display.flip()

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

    logcount2 = 0
    exit()
