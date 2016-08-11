#!/usr/bin/python
#arquivo ansible.py eh para automatizar tarefas

import sys
from Modulos.SSH import SSH
from Classes.usuarios import Usuario
from Classes.servidores import Servidor


class AdmSSH:
    def switch(self, x):
        try:
            usuario_obj = Usuario()
            servidor_obj = Servidor()
            dicionario_funcoes ={1:usuario_obj.cadastrar,
                                 2:usuario_obj.listar,
                                 3:usuario_obj.remover,
                                 4:servidor_obj.cadastrar,
                                 5:servidor_obj.listar,
                                 6:servidor_obj.remover,
                                 7:self.sair
                                }
            dicionario_funcoes[x]() 
        except Exception as e:
            print "Opcao invalida",e

    def menu(self):
        print "1- Cadastrar usuario"
        print "2- Listar usuario"
        print "3- Remover usuario"
        print "4- Cadastrar servidores"
        print "5- Listar servidores"
        print "6- Remover servidor"
        print "7- Sair"

    def sair():
        sys.exit()

if __name__ == '__main__': #defini 2 comportamento dif = 1- linha comando 2-
    admssh = AdmSSH()
    while True:
        admssh.menu()            
        opcao = int(raw_input("<< Digite a opcao desejada: "))
        admssh.switch(opcao)



executa_comando ("ip a")

''''import paramiko #tem a confirmacao parecido com ssh!
from datetime import datetime, timedelta #timedelta parte2
import sys #parte3
client = paramiko.SSHClient() #le o arquivo known_hosts
client.load_system_host_keys() #aceita fingerprint automaticamente 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#para new servers '''

#conecta na maquina:
'''client.connect(hostname="127.0.0.1",username="root",password="4linux")'''
#executa o comando:
'''acesso = datetime(2016,8,03,20,00,00) #parte3
expira = datetime(2016,8,03,21,00,00) #parte3
if(expira - acesso).total_seconds() >= 3600:
    print "Seu token expirou!", (expira-acesso)
    sys.exit()
log = datetime.now() #parte2
stdin,stdout,stderr = client.exec_command("pwd") '''
# exibe valores:
## parte1
'''print stderr.read(),stdout.read()
print "Certo: ",stdout.read()
print "Falhou: ",stdout.read()'''

## parte2
'''if stderr.channel.recv_exit_status() !=0: #se o erro for diferente de 0..
    print stderr.read()
else:
    print stdout.read()
    print "Executado as: ",log + timedelta(7) #data de hoje + 7 dias'''
## parte3
'''if stderr.channel.recv_exit_status() !=0: #se o erro for diferente de 0..
    print stderr.read()
else:
    print stdout.read()
    print "Executado as: ",log + timedelta(7) #data de hoje + 7 dias '''
