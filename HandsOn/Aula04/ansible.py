#!/usr/bin/python
#arquivo: ansible.pyy

#dentro da pasta modulos
from modulos.SSH import executa_comando
from modulos.usuarios import cadastrar_usuario, listar_usuario, remover_usuario, autenticar_usuario
from modulos.servidores import cadastrar_servidor, listar_servidor, remover_servidor



#executa_comando("pwd")


def switch(x):
    try:
        dicionario_funcoes = {1:cadastrar_usuario,
                              2:listar_usuario,
                              3:remover_usuario,
                              4:cadastrar_servidor,
                              5:listar_servidor,
                              6:remover_servidor}
        dicionario_funcoes[x]()

    except ValueError as e:
        print "caracter Invalido"

    except Exception as e:
        print "Opcao Invalida", e

    finally:
        print "Processando a requisicao"



def menu():
    print("1 -  Cadastrar SysAdmin")
    print("2 -  Listar SysAdmin")
    print("3 -  Remover SysAdmin")
    print("4 -  Cadastrar Servidor")
    print("5 -  Listar Servidor")
    print("6 -  Remover Servidor")
    print("7 -  Sair")




if __name__=="__main__":
    while True:
        #opcao = int(raw_input("Digite a opcao desejada: "))
        opcao = input("Digite a opcao desejada: ")
        switch(opcao)






