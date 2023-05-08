"""
Function Netmiko Connection
"""
from dotenv import load_dotenv
load_dotenv()
import os

username = os.getenv("USERNAME")
passwd = os.getenv("PASSWORD")
secret = os.getenv("SECRET")

# Device connection
nb_api = ["172.20.201.31"]

def netmiko_asa(ip):
    return {
            'device_type': 'cisco_asa',
            'ip': ip,
            'username': username,
            'password': passwd,
            'secret': passwd
             }


#username = os.getenv("USERNAME")
#passwd = os.getenv("PASSWD")
#secret = os.getenv("SECRET")

#user_lab = os.getenv("USER_LAB")
#pass_lab = os.getenv("PASS_LAB")
#
#user = os.getenv("USERNAME")
#passwd = os.getenv("PASSWORD")
#secret = os.getenv("SECRET")

#def netmiko_lab(ip):
#    return {
#            'device_type': 'cisco_ios',
#            'ip': ip,
#            'username': user_lab,
#            'password': pass_lab,
#             }
#
#def netmiko_a10(ip):
#    return {
#            'device_type': 'a10',
#            'ip': ip,
#            'username': username,
#            'password': passwd,
#            'secret': secret
#             }
#
## IOS-XR module works from many softwares as IOS, IOS-XR, NXOS, DellOS10
#def netmiko_iosxr(ip):
#    return {
#            'device_type': 'cisco_xr',
#            'ip': ip,
#            'username': username,
#            'password': passwd,
#             }

#def netmiko_nxos(ip):
#    return {
#            'device_type': 'cisco_nxos',
#            'ip': ip,
#            'username': username,
#            'password': passwd,
#             }
