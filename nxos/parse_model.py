import re

def parse_model_ios(text):
    """
    C2960S Software (C2960S-UNIVERSALK9-M), Version 12.2(55)SE5, RELEASE SOFTWARE (fc1)
    """
    model_regex = re.compile(r'Version (?P<version>\S........)')
parse_model_ios()

def parse_model_iosxr(text):
    """
    Cisco IOS XR Software, Version 7.0.2
    """
    model_regex = re.compile(r'Cisco\s+.........................(?P<version>.....)')
parse_model_iosxr()

def parse_model_nxos(text):
    """
    NXOS image file is: bootflash:///nxos.9.2.1.bin
    """
    model_regex = re.compile(r'NXOS image file is: bootflash.........(?P<version>.....)')
parse_model_nxos
