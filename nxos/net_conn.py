"""
Function Netmiko Connection
"""

from netmiko import ConnectHandler
from dotenv import load_dotenv
load_dotenv()
import os
import paramiko

user_os10 = os.getenv("USER_OS10")
pass_os10 = os.getenv("PASS_OS10")

user_idc = os.getenv("USERNAME")
pass_idc = os.getenv("PASSWORD")
secret = os.getenv("SECRET")

def netmiko_dellos10(ip):
    return {
            'device_type': 'dell_os10',
            'ip': ip,
            'username': user_os10,
            'password': pass_os10,
             }

def netmiko_ios(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': user_idc,
            'password': pass_idc,
             }

def netmiko_a10(ip):
    return {
            'device_type': 'a10',
            'ip': ip,
            'username': user_idc,
            'password': pass_idc,
            'secret': secret
             }

def netmiko_conn_rt_ncs(ip):
    return {
            'device_type': 'cisco_xr',
            'ip': ip,
            'username': user_idc,
            'password': pass_idc,
             }
