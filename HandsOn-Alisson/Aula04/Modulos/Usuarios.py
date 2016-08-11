#!/usr/bin/python

import json

def ler_banco():
    with open("banco.json","r") as f:
        #print type(f.read())
        banco = json.loads(f.read())
    return banco

def escrever_banco(dado):
    with open("banco.json","w") as f:
        dado = json.dumps(dado)
        f.write(dado)

def cadastrar_usuario():
    print __name__
    banco = ler_banco()
    #  {"usuarios":[]}
    usuario = {}
    usuario['login'] = raw_input("Digite o login do usuario: ")
    # {"login":"alisson"}
    usuario['senha'] = raw_input("Digite a senha:")
    # {"login":"alisson","senha":"4linux"}
    banco['usuarios'].append(usuario)
    #  {"usuarios":[{"login":"alisson","senha":"4linux"}]}
    escrever_banco(banco)


def listar_usuario():
    banco = ler_banco()
    
    for i,u in enumerate(banco.get("usuarios")):
        print "%s - %s"%(i,u.get("login"))

def remover_usuario():
    listar_usuario()
    indice = input("Digite o id do usuario: ")
    banco = ler_banco()
    banco["usuarios"].pop(indice)
    escrever_banco(banco)

if __name__ == '__main__':
    print __name__
    cadastrar_usuario()








