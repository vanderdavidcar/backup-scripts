from netmiko import ConnectHandler
import net_conn
from datetime import date
from dotenv import load_dotenv
load_dotenv()


# Checks if the folder exists, if not, it creates it.
#if not os.path.exists('/files/backups/mgmt-arq-cloud/' + str(date.today())):
#   os.makedirs('/files/backups/mgmt-arq-cloud/' + str(date.today()))

# Current time and formats it to the North American time of Month, Day, and Year.
now = date.today()

with open ('devices') as f:
    	lines =f.read().splitlines()
print (lines)

for ip in lines:
    # IOSXR modulo works from many softwares (IOS. IOS-XR, NXOS, DellOS10)
    iosxr = net_conn.netmiko_iosxr(ip)
    print ("Connecting to " + str(ip))
    
    net_connect = ConnectHandler(**iosxr)
    output = net_connect.send_command("show running")
    print(output)
    
    # Backup files .cfg
    backupFile = open(f"/home/chetos/projetos-git/backup-scripts/{ip}.cfg", "w+")
    backupFile.write(output)
