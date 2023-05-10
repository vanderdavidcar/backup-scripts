from netmiko import ConnectHandler
import net_conn
import re

hosts = ['bsl-vfw-asa01', 'bsl-vfw-asa02']
def bkp_asaperimetral():
    for ip in hosts:
        print(ip)
        ios_device = net_conn.netmiko_asa(ip)
        net_connect = ConnectHandler(**ios_device)

        # Show running in a single devices
        asaperimentral = net_connect.send_command('show running-config')
        print(asaperimentral)
        #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
        backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{ip}.cfg', "w+")
        backupFile.write(asaperimentral)
        backupFile = open(f'/home/chetos/projetos-git/backup-scripts/{ip}.cfg', "w+")
        print(f"Outputted to {ip}.cfg")
        backupFile.write(asaperimentral)
bkp_asaperimetral()

def bkp_contexts():
    for ip in hosts:
        print(ip)
        ios_device = net_conn.netmiko_asa(ip)
        net_connect = ConnectHandler(**ios_device)
        net_connect.enable()

        changeto = net_connect.send_command('changeto system')
        context_count = net_connect.send_command('show context count')
        print(context_count)

        multicontext = net_connect.send_command('show run context | in context')
        
        # Regex pattern to find contexts in device
        regex = re.compile(r"context (?P<contexts>\S+)")
        match = regex.search(multicontext)
        contexts = re.findall(regex, multicontext)
        print(contexts)

    for i in contexts:
        for dev in hosts:
            print (i)
            changeto_context = net_connect.send_command(f"changeto context {i}")
            showrun_contexts = net_connect.send_command("show running-config")
            backupFile = open(f'/mnt/c/vanderson/codes/projetos-git/public/backup-scripts/{dev}-{i}.cfg', "w+")
            #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
            backupFile.write(i)
            print(f"Outputted to {i}.cfg")
            print(showrun_contexts)

        print (i)
        changeto_context = net_connect.send_command(f"changeto context {i}")
        showrun_contexts = net_connect.send_command("show running-config")
        #backupFile = open(f'/files/backups/mgmt-arq-cloud/{ip}.cfg', "w+")
        backupFile = open(f'/home/chetos/projetos-git/backup-scripts/{i}.cfg', "w+")
        backupFile.write(showrun_contexts)
        print(f"Outputted to {i}.cfg")
        print(showrun_contexts)
bkp_contexts()