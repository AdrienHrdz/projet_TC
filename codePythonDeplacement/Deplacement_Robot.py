
import paramiko


server='192.168.169.212'
usr='pi'
psswd='raspberry'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=usr, password=psswd)
print('Connecté')
def fonctionnement_normal():
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
    return ssh_stdin, ssh_stdout, ssh_stderr

ssh1,ssh2,ssh3 =fonctionnement_normal()
print(ssh2)
ssh2.read()