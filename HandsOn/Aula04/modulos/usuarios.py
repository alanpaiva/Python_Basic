#!/usr/bin/python

import json

def ler_banco():
    #abrindo o arquivo json
    with open("banco.json","r") as f:
        #print type(f.read())
        banco = json.loads(f.read())
    return banco

def escrever_banco(dado):
    with open("banco.json","w") as f:
        dado = json.dumps(dado)
        f.write(dado)
        


def cadastrar_usuario():
    banco = ler_banco()
    #{"usuarios": []}
    usuario = {}
    usuario["login"] = raw_input("Digite o usuario: ")
    #{"login":"Alex"}
    usuario["senha"] = raw_input("Digite a senha: ")
    #{"login":"Alex","senha":"*****"}
    banco["usuarios"].append(usuario)
    #{"usuarios": [{"login":"Alex","senha":"*****"}]}
    escrever_banco(banco)
    print("Sysadmin "+ usuario["login"] + " cadastrado")



def listar_usuario():
    banco = ler_banco()
    
    for i,u in enumerate(banco.get("usuarios")):
        print "%s - %s" %(i, u.get("login"))

    #raw_input("Presione enter para coninuar...")


def remover_usuario():
    listar_usuario()
    id = input("Digite o ID que deseja remover: ")

    banco = ler_banco()

    banco["usuarios"].pop(id)


    escrever_banco(banco)

    #banco.get("usuarios").get("login")

    #banco.get("usuarios").pop(id)



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


