#!/usr/bin/python

import paramiko


def executa_comando(cmd):

    client =  paramiko.SSHClient()

    #le o arquivo know_hosts
    client.load_system_host_keys() 

    # aceita o fingerprint automaticamente
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #conecta na maquina
    client.connect(hostname="192.168.0.2", username="forlinux", password="4linux")

    #executa comando
    stdin, stdout, stderr = client.exec_command(cmd)


    # No bash do linux, a variavel "$?" retorna o cod de erro.
    # Zero significa que foi executado
    if stderr.channel.recv_exit_status() != 0:
        print "Falhou: ",stderr.read()
    else:
        print  stdout.read(), " Executado as " #, log + timedelta(7)



#print "Importando arquivo do SSH"
#print __name__

