#!/usr/bin/python

import json

def ler_banco():
    #abrindo o arquivo json
    with open("banco.json","r") as f:
        print type(f.read())
        banco = json.loads(f.read())
    return banco

def escrever_banco(dado):
    with open("banco.json","w") as f:
        dado = json.dumps(dado)
        f.write(dado)


def cadastrar_servidor():
    print("Cadastrar Servidor")

def listar_servidor():
    print("Listar Servidor")

def remover_servidor():
    print("remover Servidor")
        
