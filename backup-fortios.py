from netmiko import ConnectHandler
import net_conn

fw = ['br-lp-spah06-fw01', 'br-lp-spag06-fw02']

def bkp_fortios():
    for ip in fw:
        """
        Call function dev_connection that have all device and user information to connect and collect
        """
        fortios = net_conn.netmiko_fortios(ip)
        net_connect = ConnectHandler(**fortios)
        show_run = net_connect.send_command(f"show full-configuration")
        
        print(f"Outputted to {ip}.cfg")
        # Show running in a single devices TH3030S-1.cfg / TH3030S-2.cfg
        print(show_run)
        #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
        backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{ip}.cfg', "w+")
        backupFile.write(show_run)
bkp_fortios()