"""
Function Netmiko Connection
"""

from netmiko import ConnectHandler
from dotenv import load_dotenv
load_dotenv()
import os
import paramiko

### Netmiko Conn NXOS

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
#secret = os.getenv("SECRET")

def netmiko_connection(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
             }

### Netmiko Conn NCS br-lp-spaf06-rt-bgw01 / br-lp-spad06-rt-bgw02

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def netmiko_conn_rt_ncs(ip):
    return {
            'device_type': 'cisco_xr',
            'ip': ip,
            'username': username,
            'password': password,
             }

