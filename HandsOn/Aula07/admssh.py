#!/usr/bin/python
#arquivo ansible.py eh para automatizar tarefas

import sys
from Modulos.SSH import executa_comando
from Modulos.usuarios import cadastrar_usuario, listar_usuario, remover_usuario
from Modulos.servidores import cadastrar_servidor, listar_servidor, remover_servidor

def switch(x):
    try:
        dicionario_funcoes ={1:cadastrar_usuario,
                             2:listar_usuario,
                             3:remover_usuario,
                             4:cadastrar_servidor,
                             5:listar_servidor,
                             6:remover_servidor,
                             7:sair}
        dicionario_funcoes[x]() 
    except Exception as e:
        print "Opcao invalida",e

def menu():
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
    while True:
        menu()        
        opcao = int(raw_input("<< Digite a opcao desejada: "))
        switch(opcao)

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
