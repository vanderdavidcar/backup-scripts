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

def a10_show_run_single_dev():
    with open('hostname.txt') as f:
        devices_list = f.read().splitlines()

    for ip in devices_list:
        ios_device = net_conn.netmiko_a10(ip)
        net_connect = ConnectHandler(**ios_device)

        # Show running in a single devices TH3030S-1.cfg / TH3030S-2.cfg
        single_partition = net_connect.send_command('show running-config')
        print(single_partition)
        #backupFile = open('/files/backups/mgmt-arq-cloud/' + ip + ".cfg", "w+")
        backupFile = open('/mnt/c/vanderson/codes/projetos-git/public/bkp-scripts/a10' + ip + ".cfg", "w+")
        backupFile.write(single_partition)
        print("Outputted to " + ip + ".cfg")
a10_show_run_single_dev()


def a10_show_run_partitions():
    with open('hostname.txt') as f:
        devices_list = f.read().splitlines()

    for ip in devices_list:
        ios_device = net_conn.netmiko_a10(ip)
        net_connect = ConnectHandler(**ios_device)

    # Try to create a regex pattern instead of splip
    #multicontext = net_connect.send_command('show partition')
    #print(multicontext)
    #partitions_pattern = re.compile(r"(?P<partitions>^\S+(\s+Yes))")
    #partitions_match = partitions_pattern.search(multicontext)
    #print(partitions_match)
    #partitions = re.findall(partitions_pattern, multicontext)
    #print(partitions)

    with open(r"show_partitions.txt") as n:
        output_partition = n.read().splitlines()
        output_del_lines = output_partition[6:]
        new_list = ' '.join(output_del_lines)
        output_split = new_list.split()
        output_partition2 = output_split[0::5]
        print(output_partition2)

    for i in output_partition2:    
        print (i)
        multiples_partitions = net_connect.send_command("show running-config partition " + i)
        show_partitions = multiples_partitions
        backupFile = open('/mnt/c/vanderson/codes/projetos-git/public/bkp-scripts/' + i + ".cfg", "w+")
        backupFile.write(i)
        print("Outputted to " + i + ".cfg")
        print(show_partitions)
a10_show_run_partitions()