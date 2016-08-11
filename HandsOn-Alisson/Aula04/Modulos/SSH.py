#!/usr/bin/python

import paramiko

def executa_comando(cmd):       
    client = paramiko.SSHClient()
    # le o arquivo known_hosts
    client.load_system_host_keys()

    # aceita fingerprint automaticamente
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

    # conecta na maquina
    client.connect(hostname="192.168.0.2",
                   username="forlinux",
                   password="4linux")

    # executa comando
    stdin, stdout, stderr = client.exec_command(cmd)

    # exibe valores
    if stderr.channel.recv_exit_status() != 0:    
        return stderr.read() 
    else:
        return stdout.read()


if __name__ == '__main__':
    cmd = raw_input("Digite um comando a ser executado: ")
    executa_comando(cmd)










