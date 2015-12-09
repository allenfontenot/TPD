#!/usr/bin/env python

import smtplib
import csv


def sendmail(z1time, z2time, z3time, store, level):

    fromaddr = 'travelpathnotcomplete@gmail.com'
    msg = 'Last Travel Paths at ' + str(store) + '\nZone 1: ' + str(z1time) + ' minutes ago \nZone 2: ' + str(
        z2time) + ' minutes ago \nZone 3: ' + str(z3time) + ' minutes ago'

    msg2 = str(store) + " " + str(z1time)
    username = 'travelpathnotcomplete@gmail.com'
    password = 'gehrig10'
    server = smtplib.SMTP('smtp.gmail.com:587')

    # fills array with emails in files. must be one per line
    with open('Emails/emaillevel1.txt', 'r') as f:
        l1m = [line.strip() for line in f]

    with open('Emails/emaillevel2.txt', 'r') as f:
        l2m = [line.strip() for line in f]

    with open('Emails/emaillevel3.txt', 'r') as f:
        l3m = [line.strip() for line in f]

    server.starttls()
    server.login(username, password)

    # send one email for each address in array
    if level == 1:
        for elem in l1m:
            toaddr = elem
            server.sendmail(fromaddr, toaddr, msg)
    elif level == 2:
        for elem in l2m:
            toaddr = elem
            server.sendmail(fromaddr, toaddr, msg)

    elif level == 3:
        for elem in l3m:
            toaddr = elem
            server.sendmail(fromaddr, toaddr, msg)
    elif level == 5:
        toaddr = "allen.fontenot@gmail.com"
        server.sendmail(fromaddr, toaddr, msg2)
    server.quit()


def sendstoppedmail(store, level):
    msg3 = 'TPD at ' + str(store) + 'is not running and was rebooted'
    username = 'travelpathnotcomplete@gmail.com'
    password = 'gehrig10'
    server = smtplib.SMTP('smtp.gmail.com:587')
    fromaddr = 'travelpathnotcomplete@gmail.com'

    server.starttls()
    server.login(username, password)
    toaddr = "allen.fontenot@gmail.com"

    server.sendmail(fromaddr, toaddr, msg3)
    server.quit()
