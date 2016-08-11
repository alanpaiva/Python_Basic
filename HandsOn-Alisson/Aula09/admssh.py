#!/usr/bin/python
# arquivo: ansible.py

from Modulos.SSH import SSH
from Classes.Usuarios import Usuarios
from Classes.Servidores import Servidores

class AdmSSH:
    def switch(self,x):
        try:
            usuario_obj = Usuarios()
            servidor_obj = Servidores()
            ssh = SSH()
            dicionario_funcoes = {1:usuario_obj.cadastrar,
                                  2:usuario_obj.listar,
                                  3:usuario_obj.remover,
                                  4:servidor_obj.cadastrar,
                                  5:servidor_obj.listar,
                                  6:servidor_obj.remover,
                                  7:servidor_obj.exec_comando_servidor}
            dicionario_funcoes[x]()
        except Exception as e:
            print "Opcao invalida ",e

    def menu(self):
        print "1 - Cadastrar sysadmin"
        print "2 - listar sysadmins"
        print "3 - remover sysadmin"
        print "4 - cadastrar servidor"
        print "5 - listar servidores"
        print "6 - remover servidor"
        print "7 - Sair"

if __name__ == '__main__':
    admssh = AdmSSH()
    admssh.menu()
    while True:
        opcao = int(raw_input("Digite a opcao desejada: "))
        admssh.switch(opcao)






