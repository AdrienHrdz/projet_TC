import paramiko
import time

# adresse ip à modifier selon le serveur
server='192.168.97.212'
usr='pi'
psswd='raspberry'

remote_filename = '/home/pi/Documents/PTC/communicationPi-Ordi/GPIO_distance.txt'

## Ouverture du client SSH ##

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(server, username=usr, password=psswd)
print('Connecté')

shell = ssh_client.invoke_shell()


def lancementCollecteDonnees():
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /home/pi/Documents/PTC/recolteDonneesCapteur8051 && python3 collect_data.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def HardReset():
    global ssh_client

    # close ssh connection
    ssh_client.close()
    
    # re-open ssh connection
    #global ssh_client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server, username=usr, password=psswd)
    print("Connecté")


## Lancement de la collecte de données ##
ssh_stdin, ssh_stdout, ssh_stderr = lancementCollecteDonnees()
time.sleep(5)

"""HardReset()
time.sleep(5)

ssh_stdin, ssh_stdout, ssh_stderr = lancementCollecteDonnees()
time.sleep(5)

HardReset()"""