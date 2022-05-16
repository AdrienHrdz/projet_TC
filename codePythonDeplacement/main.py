
import paramiko
import time

# adresse ip à modifier selon le serveur
server='192.168.97.212'
usr='pi'
psswd='raspberry'

remote_filename = '/home/pi/Documents/PTC/communicationPi-Ordi/GPIO_distance.txt'

## Fonctions pour la connexion SSH ##
def OpenConnection(server, usr, psswd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server, username=usr, password=psswd)
    print('Connecté')

    return ssh_client

def ResetConnection(ssh_client):
    # close ssh connection
    ssh_client.close()
    
    # re-open ssh connection
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server, username=usr, password=psswd)
    print("Connecté")

    return ssh_client

## Fonctions pour le robot ##
def avancer(ssh_client):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 avancer.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def tourneGauche(ssh_client):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 tourneGauche.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def tourneDroite(ssh_client):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 tourneDroite.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def stop(ssh_client):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 stop.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def lancementCollecteDonnees(ssh_client):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /home/pi/Documents/PTC/recolteDonneesCapteur8051 && python3 collect_data.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr


## Ouverture du client SSH ##
ssh_client = OpenConnection(server, usr, psswd)

## Lancement de la collecte de données ##
ssh_stdin, ssh_stdout, ssh_stderr = lancementCollecteDonnees(ssh_client)
time.sleep(2)

## Boucle infinie ##
condition = True
while condition:
    ## Lecture du fichier distant ##
    sftp_client = ssh_client.open_sftp()
    remote_file = sftp_client.open(remote_filename)
    try:
        for line in remote_file:
            etat = int(line.strip())
    finally:
        remote_file.close()
        sftp_client.close()
    
    ## Traitement du déplacement ##
    
    if etat == 0:
        # Pas d'obstacle, on avance
        ssh_stdin, ssh_stdout, ssh_stderr = avancer(ssh_client)
        time.sleep(7)
        

    elif etat == 1:
        # Obstacle, on fait gaffe
        ssh_stdin, ssh_stdout, ssh_stderr = tourneDroite(ssh_client)
        time.sleep(7)

    else:
        condition = True
        ssh_client = ResetConnection(ssh_client)
        


