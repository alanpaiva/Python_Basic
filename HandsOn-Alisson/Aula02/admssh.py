#!/usr/bin/python

usuarios = []
senhas = []
servidores = []


def switch(x):
    try:
        dicionario_funcoes = {1:cadastrar_sysadmin,
                              2:listar_sysadmin,
                              3:remover_sysadmin}
        dicionario_funcoes[x]()
    except ValueError as e:
        print "Caracter invalido ",e
    except Exception as e:
        print "Opcao invalida ",e
    finally:
        print "Processando a requisicao"
    



def cadastrar_sysadmin():
    global usuarios
    global senhas
    login = raw_input("Digite o login do usuario: ")
    senha = raw_input("Digite a senha:")
    usuarios.append(login)
    senhas.append(senha)

def listar_sysadmin():
    global usuarios
    for i,u in enumerate(usuarios):
        print "%s - %s"%(i,u)

def remover_sysadmin():
    listar_sysadmin()
    indice = input("Digite o id do usuario: ")
    global usuarios
    usuarios.pop(indice)
    senhas.pop(indice)

def cadastrar_servidor():
    print "-= Autenticar Usuario =-"
    global usuarios
    global senhas
    login = raw_input("Digite o seu login: ")
    senha = raw_input("Digite a sua senha: ")
    for usuario in usuarios:
        if usuario == login:
            indice = usuarios.index(usuario)
            if usuarios[indice] == login and senhas[indice] == senha:
                print "Autenticado com sucesso"
                break
            else:
                print "Falhou ao autenticar"
                break
    else:
        print "Usuario nao encontrado"
    
print "1 - Cadastrar sysadmin"
print "2 - listar sysadmins"
print "3 - remover sysadmin"
print "4 - cadastrar servidor"
print "5 - listar servidores"
print "6 - remover servidor"
print "7 - Sair"

while True:
    opcao = int(raw_input("Digite a opcao desejada: "))
    switch(opcao)
    if opcao == 7:
        break






