sudo chmod +x /home/pi/TPD/CronScripts/dashonrestart.sh
sudo chmod +x /home/pi/TPD/CronScripts/simtp.py
sudo chmod +x /home/pi/TPD/CronScripts/logbackup.py
sudo chmod +x /home/pi/TPD/CronScripts/logbackup.sh


sudo cp /home/pi/TPD/Crons/dashonrestart /etc/cron.d/dashonrestart
sudo cp /home/pi/TPD/Crons/dashonrestart /etc/cron.d/logbackup
sudo cp /home/pi/TPD/Crons/isRunningCheck /etc/cron.d/isRunningCheck

sudo chmod +x /etc/cron.d/dashonrestart
sudo chmod +x /etc/cron.d/logbackup
sudo chmod +x /etc/cron.d/isRunningCheck
sudo chmod +x /home/pi/TPD/DU/dropbox_uploader.sh

sudo python simtp.py
