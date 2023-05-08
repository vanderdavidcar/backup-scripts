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


devices = ["TH3030S-1","TH3030S-2"]

def a10_show_run_partitions():
     for ip in devices:
        ios_device = net_conn.netmiko_a10(ip)
        net_connect = ConnectHandler(**ios_device)

        # Try to create a regex pattern instead of splip
        multicontext = net_connect.send_command('show partition')
        print(multicontext)
        pattern = re.compile(r"(?P<partitions>^\S+(\s+Yes))")
        match = pattern.search(multicontext)
        print(match)
        partitions = re.findall(pattern, multicontext)
        print(partitions)

    #with open(r"show_partitions.txt") as n:
    #    output_partition = n.read().splitlines()
    #    output_del_lines = output_partition[6:]
    #    new_list = ' '.join(output_del_lines)
    #    output_split = new_list.split()
    #    output_partition2 = output_split[0::5]
    #    print(output_partition2)

    #for i in output_partition2:
        for i in partitions:    
            print (i)
            multiples_partitions = net_connect.send_command(f"show running-config partition {i}")
            show_partitions = multiples_partitions
            #backupFile = open('/files/backups/mgmt-arq-cloud/{i}.cfg', "w+")
            backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{i}.cfg', "w+")
            backupFile.write(i)
            print(f"Outputted to {i}.cfg")
            print(show_partitions)
a10_show_run_partitions()