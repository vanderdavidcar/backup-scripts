"""
Function Netmiko Connection
"""

from dotenv import load_dotenv
load_dotenv()
import os

username = os.getenv("USERNAME")
passwd = os.getenv("PASSWD")


user_lab = os.getenv("USER_LAB")
pass_lab = os.getenv("PASS_LAB")

def netmiko_lab(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': user_lab,
            'password': pass_lab,
             }

def netmiko_a10(ip):
    return {
            'device_type': 'a10',
            'ip': ip,
            'username': username,
            'password': passwd,
            'secret': passwd
             }

# IOS-XR module works from many softwares as IOS, IOS-XR, NXOS, DellOS10
def netmiko_iosxr(ip):
    return {
            'device_type': 'cisco_xr',
            'ip': ip,
            'username': username,
            'password': passwd,
             }

def netmiko_asa(ip):
    return {
            'device_type': 'cisco_asa',
            'ip': ip,
            'username': username,
            'password': passwd,
            'secret': passwd
             }
