#!/usr/bin//python
#arquivo: ansible.pyy

#paramiko serve para executar comandos bash
import paramiko
#importa biblioteca de datetime
from datetime import datetime


client =  paramiko.SSHClient()


#le o arquivo know_hosts
client.load_system_host_keys() 

# aceita o fingerprint automaticamente
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#conecta na maquina
client.connect(hostname="127.0.0.1", username="root", password="4linux")

#executa comando
log = datetime.now()
stdin, stdout, stderr = client.exec_command("pwd")


# No bash do linux, a variavel "$?" retorna o cod de erro.
# Zero significa que foi executado
if stderr.channel.recv_exit_status() != 0:
    print "Falhou: ",stderr.read()
else:
    print  stdout.read(), " Executado as ", log



