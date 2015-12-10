
#!/usr/bin/env python

import sys
import os
sys.path.insert(0, '/home/pi/TPD')
import shutil
from settings import NSN
import datetime

date = datetime.date.today()#get day month year

#moves current travellog.csv to log folder and renames travellog.old which is initialized
#to travellog.csv. So backs up and clears the log

newFileName = 'TPDlog-' + NSN + '-' + str(date) + '.csv'
newFilePath = '/home/pi/TPD/logs/TPDlogs/'+newFileName

newFileNameDebug = 'debug-' + NSN + '-' + str(date) + '.txt'
newFilePathDebug = '/home/pi/TPD/logs/debuglogs/'+newFileNameDebug

newFileNameViolations = 'violations-' + NSN + '-' + str(date) + '.csv'
newFilePathViolations = '/home/pi/TPD/logs/violations/'+newFileNameDebug

os.rename('/home/pi/TPD/logs/travellog.csv', newFilePath)
os.rename('/home/pi/TPD/logs/debug.log', newFilePathDebug)
os.rename('/home/pi/TPD/logs/violations.csv', newFilePathViolations)

shutil.copyfile('/home/pi/TPD/logs/travellog.old', '/home/pi/TPD/logs/travellog.csv')