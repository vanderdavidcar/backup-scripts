from netmiko import ConnectHandler
import net_conn

with open('devices_bsa.txt', 'r') as f:
    nb_api = f.read().split()

def nxos_fabric():
    for ip in nb_api:
        """
        Call function dev_connection that have all device and user information to connect and collect
        """
        nxos_device = net_conn.netmiko_nxos(ip)
        net_connect = ConnectHandler(**nxos_device)
        show_run = net_connect.send_command(f"show running-config")
        
        print(f"Outputted to {ip}.cfg")
        # Show running in a single devices TH3030S-1.cfg / TH3030S-2.cfg
        print(show_run)
        #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
        backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{ip}.cfg', "w+")
        backupFile.write(show_run)
nxos_fabric()

fw = ['br-lp-spah06-fw01', 'br-lp-spag06-fw02']

def bkp_fortios():
    for ip in fw:
        """
        Call function dev_connection that have all device and user information to connect and collect
        """
        fortios = net_conn.netmiko_fortios(ip)
        net_connect = ConnectHandler(**fortios)
        show_run = net_connect.send_command(f"show running-config")
        
        print(f"Outputted to {ip}.cfg")
        # Show running in a single devices TH3030S-1.cfg / TH3030S-2.cfg
        print(show_run)
        #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
        backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{ip}.cfg', "w+")
        backupFile.write(show_run)
bkp_fortios()