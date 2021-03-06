#!/bin/bash

cd /home/pi/TPD
sudo python logbackup.py

cd /home/pi/TPD/logs
sudo touch debug.log
sudo touch violations.csv

cd /home/pi/TPD

sudo bash dropbox_uploader.sh -s -f .duconfig upload /home/pi/TPD/logs/TPDlogs/*.csv /TPDlogs-gehrig/

sudo bash dropbox_uploader.sh -s -f .duconfig upload /home/pi/TPD/logs/debuglogs/*.txt /debuglogs-gehrig/

sudo bash dropbox_uploader.sh -s -f .duconfig upload /home/pi/TPD/logs/violations/*.csv /violations-gehrig/

sudo ./simtp.py