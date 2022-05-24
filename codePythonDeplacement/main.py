import paramiko
import time

# adresse ip à modifier selon le serveur
#server='192.168.123.212'
server='192.168.232.212'
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

def OpenServer(ssh_client):
    #Ouverture du serveur pour le transfert de fichier
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('python3 -m http.server 8080')

    return ssh_stdin, ssh_stdout, ssh_stderr

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

def lancementLidar(ssh_client):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('cd /home/pi/Documents/PTC/Lidar_Python && sudo python3 getData.py')

    return ssh_stdin, ssh_stdout, ssh_stderr

## Ouverture du client SSH ##
ssh_client = OpenConnection(server, usr, psswd)

## Lancement de la collecte de données ##
ssh_stdin, ssh_stdout, ssh_stderr = lancementCollecteDonnees(ssh_client)
time.sleep(3)

## Ouverture du serveur pour le transfert de fichier ##
ssh_stdin, ssh_stdout, ssh_stderr = OpenServer(ssh_client)
time.sleep(3)

## Lancer la collecte de data  ## 
ssh_stdin, ssh_stdout, ssh_stderr = lancementLidar(ssh_client)
time.sleep(3)


## Boucle infinie ##
condition = True
while condition:
    time.sleep(4)
    ## Lecture du fichier distant ##
    sftp_client = ssh_client.open_sftp()
    remote_file = sftp_client.open(remote_filename)
    try:
        for line in remote_file:
            etat = int(line.strip())
    except:
        print("Erreur de lecture du fichier distant")
        etat = 2
    finally:
        remote_file.close()
        sftp_client.close()
    
    ## Traitement du déplacement ##
    print(etat)
    if etat == 1:
        # Pas d'obstacle, on avance
        #ssh_stdin, ssh_stdout, ssh_stderr = avancer(ssh_client)
        # time.sleep(4)
        pass
        

    elif etat == 0:
        # Obstacle, on fait gaffe
        #ssh_stdin, ssh_stdout, ssh_stderr = stop(ssh_client)
        #time.sleep(4)
        pass

    elif etat == 2:
        # Erreur de lecture du fichier distant : on relance les processus
        ssh_client = ResetConnection(ssh_client)
        ssh_stdin, ssh_stdout, ssh_stderr = lancementCollecteDonnees(ssh_client)
        time.sleep(4)
        ssh_stdin, ssh_stdout, ssh_stderr = lancementLidar(ssh_client)
        time.sleep(4)
        pass

    else:
        print("Fin programme")
        condition = False
        
        


