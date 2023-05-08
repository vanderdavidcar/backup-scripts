from netmiko import ConnectHandler
import dev_connection

def asa5585_perimeter():
    for ip in dev_connection.nb_api:
        """
        Call function dev_connection that have all device and user information to connect and collect
        """
        net_connect = ConnectHandler(**dev_connection.iosv)
        net_connect.enable()

        term_pager0 = net_connect.send_command("terminal pager 0")
        # Command executed on Cisco ASA to find a costumer configuration
        show_run = net_connect.send_command(f"show running-config")
        
        print(f"Outputted to {ip}.cfg")
        # Show running in a single devices TH3030S-1.cfg / TH3030S-2.cfg
        print(show_run)
        #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
        backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{ip}.cfg', "w+")
        backupFile.write(show_run)
asa5585_perimeter()