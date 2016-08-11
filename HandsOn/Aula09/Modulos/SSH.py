#!/usr/bin/python
#esse modulo so vai conectar no servidor e printar na tela..

import paramiko

class SSH:
    def __init__(self):
        self.client = paramiko.SSHClient() 
        #le o arquivo known_hosts        
        self.client.load_system_host_keys() 
        #aceita fingerprint automaticamente 
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #p.nw servers
        #conecta na maquina:
        self.client.connect(hostname="192.168.0.2",
                            username="forlinux",
                            password="4linux")


    def executa_comando(self, cmd):
        
        #executa o comando:
        stdin,stdout,stderr = self.client.exec_command(cmd)

        # exibe valores:
        ## parte3
        #se o erro for diferente de 0..
        if stderr.channel.recv_exit_status() !=0: 
            return stderr.read()
        else:
            return stdout.read()



if __name__ == '__main__':
    print "Esse arquivo foi excutado pelo terminal"
#excuta_comando("hostname")
#print __name__
