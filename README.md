# Backup scripts written by python and ansible

Scripts in using function to get backup devices in python to devices: </br>

A10-networks:  Partitions backups splited by names</br>
Cisco Adaptive Security Appliance (ASA): backups of multiples contexts</br>
Cisco Nexus: backup all devices

## .env

To protect credentials leaking, create a .env file with variables that will be used to connect on devices (USER_LAB/PASS_LAB).

e.g
USER_LAB=vanderson
PASS_LAB=cisco

## net_conn.py

A module imported in files ".py" which needed a credentials to connect on devices.


