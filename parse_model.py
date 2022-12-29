import re

def ios():
    """
    System image file is "unix:/opt/unetlab/addons/iol/bin/L2-ADVENTERPRISEK9-M-15.2-IRON-20151"
    """
    regex = re.compile(r'System image file is (\S*)')
ios()
