#!/usr/bin/env bash
sudo chmod +x /home/pi/TPD/dashonrestart.sh
sudo chmod +x /home/pi/TPD/logbackup.py
sudo chmod +x /home/pi/TPD/logbackup.sh
sudo chmod +x /home/pi/TPD/Running_Check.py
sudo chmod +x /home/pi/TPD/Running_Check.sh
sudo chmod +x /home/pi/TPD/simtp.py
sudo chmod +x /home/pi/TPD/amreboot.sh


sudo cp /home/pi/TPD/Crons/dashonrestart /etc/cron.d/dashonrestart
sudo cp /home/pi/TPD/Crons/logbackup /etc/cron.d/logbackup
sudo cp /home/pi/TPD/Crons/isRunningCheck /etc/cron.d/isRunningCheck
sudo cp /home/pi/TPD/Crons/amreboot /etc/cron.d/isRunningCheck/amreboot

sudo chmod +x /etc/cron.d/dashonrestart
sudo chmod +x /etc/cron.d/logbackup
sudo chmod +x /etc/cron.d/isRunningCheck
sudo chmod +x /etc/cron.d/amreboot
sudo chmod +x /home/pi/TPD/dropbox_uploader.sh

sudo python simtp.py
