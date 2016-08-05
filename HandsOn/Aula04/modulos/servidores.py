#!/usr/bin/python

import json

from modulos.usuarios import ler_banco, escrever_banco


def cadastrar_servidor():

    #le o arquivo json
    banco = ler_banco()

    #cria um item
    servidor = {}
    servidor["hostname"] = raw_input("Digite o hostname: ")
    servidor["descricao"] = raw_input("Digite a descricao: ")

    #adiciona o item criado na variavel que contem o json
    banco["servidores"].append(servidor)

    #escreve a variavel do json, de volta no arquivoo
    escrever_banco(banco)
    print("Servidor "+ servidor["hostname"] + " cadastrado")



def listar_servidor():
    print("== Listar Servidor ==")

    banco = ler_banco()
    for i,u in enumerate(banco.get("servidores")):
        print "%s - %s"%(i,u.get("hostname"))
    
    print __name__
    raw_input("Presione enter para continuar")


def remover_servidor():
    print("== Remover Servidor ==")
    listar_servidor()

    id = input("Digite o ID que deseja remover: ")
    banco = ler_banco()

    banco["servidores"].pop(id)

    escrever_banco(banco)        


