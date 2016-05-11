#!/usr/bin/env bash
sudo rm /home/pi/TPD/Emails/emaillevel1.txt
sudo rm /home/pi/TPD/Emails/emaillevel2.txt

sudo touch /home/pi/TPD/Emails/emaillevel1.txt
sudo touch /home/pi/TPD/Emails/emaillevel2.txt

sudo python set_email_tpd.py
