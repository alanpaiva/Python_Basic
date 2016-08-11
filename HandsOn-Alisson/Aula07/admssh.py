#!/usr/bin/python
# arquivo: ansible.py

from Modulos.SSH import executa_comando
from Modulos.Usuarios import cadastrar_usuario, listar_usuario, remover_usuario
from Modulos.Servidores import cadastrar_servidor, listar_servidor, remover_servidor, exec_comando_servidor

def switch(x):
    try:
        dicionario_funcoes = {1:cadastrar_usuario,
                              2:listar_usuario,
                              3:remover_usuario,
                              4:cadastrar_servidor,
                              5:listar_servidor,
                              6:remover_servidor,
                              7:exec_comando_servidor}
        dicionario_funcoes[x]()
    except Exception as e:
        print "Opcao invalida ",e

def menu():
    print "1 - Cadastrar sysadmin"
    print "2 - listar sysadmins"
    print "3 - remover sysadmin"
    print "4 - cadastrar servidor"
    print "5 - listar servidores"
    print "6 - remover servidor"
    print "7 - Sair"

if __name__ == '__main__':
    menu()
    while True:
        opcao = int(raw_input("Digite a opcao desejada: "))
        switch(opcao)






