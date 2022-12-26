from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
import net_conn_def
from parse_model import parse_model_iosxr, parse_model_nxos
import re 

start_time = datetime.now()
print (start_time)

with open ('devices_iosxr.txt') as f:
    	lines =f.read().splitlines()
print (lines)

for devices in lines:
    net_connect = ConnectHandler(**iosv)
    #show version of devices to parse version
    sw_ver = net_connect.send_command("show version")
    
    # store as variable
    sw_outputs = sw_ver
    print(sw_outputs)

    if parse_model_nxos == 'NXOS image file is: bootflash:///nxos.9.2.1.bin':
        iosxr = net_conn_def.netmiko_conn(ip)
        print ("Connecting to " + str(ip))

        # Pattern to use regex in a file iosxr_version.txt
        version_pattern = re.compile(r"Cisco IOS XR Software, Version (?P<version>\S....)")
        iosxr_version = version_pattern.search(results)
        
        
        version_pattern = parse_model_nxos
        nxos_version = version_pattern.search(results)
        print(nxos_version)
