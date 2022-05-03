
import paramiko
import time


def avancer():
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 avancer.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def tourneGauche():
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 tourneGauche.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def tourneDroite():
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 tourneDroite.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def stop():
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cd /home/pi/Documents/PTC/configGPIO && python3 stop.py')
    
    return ssh_stdin, ssh_stdout, ssh_stderr

def affichage_pwd():
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('pwd')
    
    return ssh_stdin, ssh_stdout, ssh_stderr



server='192.168.169.212'
usr='pi'
psswd='raspberry'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=usr, password=psswd)
print('Connecté')


ssh1,ssh2,ssh3 =avancer()
time.sleep(10)
ssh1,ssh2,ssh3 =tourneGauche()
time.sleep(10)
ssh1,ssh2,ssh3 =tourneDroite()


