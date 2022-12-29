from netmiko import ConnectHandler
from getpass import getpass
import net_conn
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
import os

start_time = datetime.now()

with open("devices") as f_dellos10:
    devices = f_dellos10.read().splitlines()

# NX-OS module 
def dev_conn_ios(ips, model):
    for ips in devices:
        # call net_conn module there are all connection model (nxos, ios, dellos) 
        iosv = net_conn.netmiko_conn_ncs(ips)
        print(f"\n{'#'*79}\nConnecting to device model: {model.upper()}\nHostname: {ips}\n")
        net_connect = ConnectHandler(**iosv)
        command1 = net_connect.send_command('show version')
        print(command1)
        
        end_time = datetime.now()
        print("Total time: {}".format(end_time - start_time))

dev_conn_ios(devices, "nxos")
