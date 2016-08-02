#!/usr/bin/python


def switch(x):
    dicionario_funcoes = {1:cadastrar_sysadmin,
                          2:listar_sysadmin,
                          3:remover_sysadmin,
                          4:cadastrar_servidor,
                          5:listar_servidor,
                          6:remover_servidor,
                          7:sair}
    dicionario_funcoes[x]()



def cadastrar_sysadmin():
    print("Cadastrar sysadmin")

def listar_sysadmin():
    print("Listar sysadmin")

def remover_sysadmin():
    print("remover sysadmin")

def cadastrar_servidor():
    print("Cadastrar Servidor")

def listar_servidor():
    print("Listar Servidor")

def remover_servidor():
    print("remover Servidor")

def sair():
    print("sair")



print("1 -  Cadastrar SysAdmin")
print("2 -  Listar SysAdmin")
print("3 -  Remover SysAdmin")
print("4 -  Cadastrar Servidor")
print("5 -  Listar Servidor")
print("6 -  Remover Servidor")
print("7 -  Sair")


while True:
    #opcao = int(raw_input("Digite a opcao desejada: "))
    opcao = input("Digite a opcao desejada: ")
    switch(opcao)

    if opcao==7:
        break



