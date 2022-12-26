"""
Function Netmiko Connection
"""

from netmiko import ConnectHandler
#from dotenv import load_dotenv
#load_dotenv()
import os

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
