#!/usr/bin/env python
import csv
import datetime
from settings import zone1
from settings import zone2
from settings import zone3

NSN = 'SIM'
#zone1 = 'Lobby'
#zone2 = 'Stockroom'
#zone3 = 'Drive Thru'
time1 = []
time2 = []
time3 = []

FMT = '%Y-%m-%d %H:%M:%S.%f'

print "simpush"
outputFile = open('logs/travellog.csv', 'a')
now = datetime.datetime.now()

outputWriter = csv.writer(outputFile)
outputWriter.writerow([now, zone1, 60, NSN])
outputWriter.writerow([now, zone2, 60, NSN])
outputWriter.writerow([now, zone3, 60, NSN])

outputFile.close()
