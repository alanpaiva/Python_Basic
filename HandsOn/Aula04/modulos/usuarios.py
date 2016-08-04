#!/usr/bin/python

import json

def ler_banco():
    #abrindo o arquivo json
    with open("banco.json","r") as f:
        banco = json.loads(f.read())
    return banco

def escrever_banco(dado):
    with open("banco.json","w") as f:
        dado = json.dumps(dado)
        f.write(dado)
        


def cadastrar_usuario():
    banco = ler_banco()
    usuario = {}
    usuario["login"] = raw_input("Digite o usuario: ")
    usuario["senha"] = raw_input("Digite a senha: ")
    banco["usuarios"].append(usuario)
    
    escrever_banco(banco)
    print("Sysadmin "+ usuario["login"] + " cadastrado")



def listar_usuario():
    global usuarios
    #ENUMERATE (passando i) 
    #serve para numerar  itens e retornar o numero e o item
    for i,u in enumerate(usuarios):
        print("%s - %s"%(i,u))


def remover_usuario():
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


