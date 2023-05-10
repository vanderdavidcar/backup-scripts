"""
Function Netmiko Connection
"""
from dotenv import load_dotenv
load_dotenv()
import os

asa_username = os.getenv("ASAUSERNAME")
asa_passwd = os.getenv("ASAPASSWD")

idcuser = os.getenv("IDCUSERNAME")
idcpass = os.getenv("IDCPASSWORD")

bkpuser = os.getenv("IDCUSERNAME")
bkppass = os.getenv("IDCPASSWORD")

# Device connection
nb_api = ["172.20.201.31"]

def netmiko_asa(ip):
    return {
            'device_type': 'cisco_asa',
            'ip': ip,
            'username': asa_username,
            'password': asa_passwd,
            'secret': asa_passwd
             }

# IOS-XR module works from many softwares as IOS, IOS-XR, NXOS, DellOS10
def netmiko_iosxr(ip):
    return {
            'device_type': 'cisco_xr',
            'ip': ip,
            'username': idcuser,
            'password': idcpass,
             }

def netmiko_nxos(ip):
    return {
            'device_type': 'cisco_nxos',
            'ip': ip,
            'username': idcuser,
            'password': idcpass,
             }

def netmiko_fortios(ip):
    return {
            'device_type': 'fortinet',
            'ip': ip,
            'username': bkpuser,
            'password': bkppass,
             }
