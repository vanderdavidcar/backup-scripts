from netmiko import ConnectHandler
from datetime import date
import net_conn
import os
import re

#Import dotenv to manage user/passwd 
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

# Current time and formats it to the North American time of Month, Day, and Year.
now = date.today()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
secret = os.getenv("SECRET")

def bkp_asaperimetral():
    with open('hostname.txt') as f:
        devices_list = f.read().splitlines()

    for ip in devices_list:
        ios_device = net_conn.netmiko_ios(ip)
        net_connect = ConnectHandler(**ios_device)

        # Show running in a single devices
        asaperimentral = net_connect.send_command('show running-config')
        print(asaperimentral)
        backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}', "w+")
        backupFile.write(asaperimentral)
        print(f"Outputted to {ip}.cfg")
bkp_asaperimetral()


def bkp_contexts():
    with open('hostname.txt') as f:
        devices_list = f.read().splitlines()

    for ip in devices_list:
        ios_device = net_conn.netmiko_ios(ip)
        net_connect = ConnectHandler(**ios_device)

    # Try to create a regex pattern instead of splip
    multicontext = net_connect.send_command('changeto system')
    context_count = net_connect.send_command('show context count')
    multicontext = net_connect.send_command('show context | in context')
    print(multicontext)
    partitions_pattern = re.compile(r"context (?P<contexts>(\S+)")
    partitions_match = partitions_pattern.search(multicontext)
    print(partitions_match)
    contexts = re.findall(partitions_pattern, multicontext)
    print(contexts)

    for i in contexts:    
        print (i)
        multiples_contexts = net_connect.send_command(f"show running-config {i}")
        show_partitions = multiples_contexts
        backupFile = open(f"/files/backups/mgmt-arq-cloud/{i}.cfg", "w+")
        backupFile.write(i)
        print("Outputted to " + i + ".cfg")
        print(show_partitions)
bkp_contexts()