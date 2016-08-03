#!/usr/bin/python

usuarios=[]
senhas=[]
servidores=[]





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
    global usuarios
    login = raw_input("Digite o usuario: ")
    senha = raw_input("Digite a senha: ")

    usuarios.append(login)
    senhas.append(senha)
    print("Sysadmin "+ login + " cadastrado")



def listar_sysadmin():
    global usuarios
    #ENUMERATE (passando i) 
    #serve para numerar  itens e retornar o numero e o item
    for i,u in enumerate(usuarios):
        print("%s - %s"%(i,u))


def remover_sysadmin():
    global usuarios    
    listar_sysadmin()
    id = input("Digite o ID que deseja remover: ")
    print("Usuario " + usuarios[id] + " removido")
    usuarios.pop(id)
    senhas.pop(id)


def autenticar_usuario(login, senha):
    global usuarios
    global senhas

    for user in usuarios:
        if user==login:
            indice = usuarios.index(user)
            if usuarios[indice] == login and senhas[indice]==senha:
                return True
    '''
    for i, u in enumerate(usuarios):
        if login==usuarios[i] and senha==senhas[i] :
            return True
    '''
    return False



def cadastrar_servidor():
    print("== Autenticar usuario ==")
    login = raw_input("Digite o seu login: ")
    senha = raw_input("Digite a sua senha: ")
    if autenticar_usuario(login,senha):
        servidor = raw_input("Digite o servidor: ")
        servidores.append(servidor)
        print ("Serrvidor " + servidor + " cadastrado")

    else:
        print "Falha na autenticacao!"



def listar_servidor():
    global servidores
    for s in servidores:
        print(s)

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



