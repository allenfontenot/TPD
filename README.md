# TravelDash
Travel Path Dashboard

1. Install NOOBS
2. Open Console
3. sudo apt-get update
4. sudo apt-get upgrade
5. sudo raspi-config
6. change time zone
7. change password
8. disable overscan
9. sudo nano /etc/rsyslog.conf
10. comment out last 4 lines
      #daemon.*;mail.*;\
      #news.err;\
      #*.=debug;*.=info;\
      #*.=notice;*.=warn       |/dev/xconsole
10. sudo git clone http://www.github.com/allenfontenot/TPD
11. cd TPD
12. sudo nano settings.py
13. change NSN and email time settings
14. cd Emails
15. sudo nano emaillevel1.txt
16. add 1 email per line
17. sudo nano emaillevel2.txt
18. add 1 email per line
19. sudo nano emaillevel3.txt add doug
20. sudo chmod +x cronsetup.sh 
21. sudo ./cronsetup.sh
22. sudo reboot

add port forward from 22 to 2022 with ip of TPD
