#!/usr/bin/python
#esse modulo so vai conectar no servidor e printar na tela..

import paramiko

def executa_comando(cmd):
    
    client = paramiko.SSHClient() #le o arquivo known_hosts
    client.load_system_host_keys() #aceita fingerprint automaticamente 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#p.nw servers

    #conecta na maquina:
    client.connect(hostname="192.168.0.2",username="forlinux",password="4linux")
    #executa o comando:
    stdin,stdout,stderr = client.exec_command(cmd)

    # exibe valores:
    ## parte3
    if stderr.channel.recv_exit_status() !=0: #se o erro for diferente de 0..
        print stderr.read()
    else:
        print stdout.read()

if __name__ == '__main__':
    print "Esse arquivo foi excutado pelo terminal"
#excuta_comando("hostname")
#print __name__
