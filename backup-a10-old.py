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

devices = ["TH3030S-1", "TH3030S-2"]

def a10_show_run_single_dev():
    for ip in devices:
        ios_device = net_conn.netmiko_a10(ip)
        net_connect = ConnectHandler(**ios_device)
        print(f"Outputted to {ip}.cfg")
        # Show running in a single devices TH3030S-1.cfg / TH3030S-2.cfg
        single_partition = net_connect.send_command('show running-config')
        print(single_partition)
        #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
        backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{ip}.cfg', "w+")
        backupFile.write(single_partition)
a10_show_run_single_dev()


def a10_show_run_partitions():
    for ip in devices:
        ios_device = net_conn.netmiko_a10(ip)
        net_connect = ConnectHandler(**ios_device)
        print(f"Outputted to {ip}.cfg")
        # Try to create a regex pattern instead of splip
        multicontext = net_connect.send_command('show partition')
        file = open('show_partitions.txt', "w+")
        file.write(multicontext)

        #partitions_pattern = re.compile(r"(?P<partitions>^\S+(\s+Yes))")
        #partitions_match = partitions_pattern.search(multicontext)
        #print(partitions_match)
        #partitions = re.findall(partitions_pattern, multicontext)
        #print(partitions)

        n = open(r"show_partitions.txt")
        output_partition = n.read().splitlines()
        output_del_lines = output_partition[6:]
        new_list = ' '.join(output_del_lines)
        output_split = new_list.split()
        output_partition2 = output_split[0::5]
        print(output_partition2)

    for i in output_partition2:
        for hosts in devices:
            print(f"Outputted to {i}.cfg")
            multiples_partitions = net_connect.send_command(f"show running-config partition {i}")
            print(multiples_partitions)
            #backupFile = open(f'/files/backups/mgmt-arq-cloud/A10-{hosts}-{ip}.cfg', "w+")
            backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/A10-{hosts}-{i}.cfg', "w+")
            backupFile.write(multiples_partitions)
            
a10_show_run_partitions()