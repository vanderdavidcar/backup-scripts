from netmiko import ConnectHandler
import net_conn_def
import time, os
from datetime import date, datetime

# Checks if the folder exists, if not, it creates it.
#if not os.path.exists('/files/backups/mgmt-arq-cloud/' + str(date.today())):
#   os.makedirs('/files/backups/mgmt-arq-cloud/' + str(date.today()))

# Current time and formats it to the North American time of Month, Day, and Year.
now = date.today()

with open ('devices.txt') as f:
    	lines =f.read().splitlines()
print (lines)

for ip in lines:
    iosv = net_conn_def.netmiko_connection(ip)
    print ("Connecting to " + str(ip))
    net_connect = ConnectHandler(**iosv)
    output = net_connect.send_command("show running")
    for out in output:
            backupFile = open('/mnt/c/vanderson/codes/projetos-git/public/bkp-scripts/nxos/' + ip +  ".cfg", "w+")
            backupFile.write(output)

