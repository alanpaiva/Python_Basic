#!/usr/bin/python

import json

from modulos.usuarios import ler_banco, escrever_banco
from modulos.docker import criar_container, remover_container, pegar_ip_container, executa_comando
from modulos.SSH import executa_comando as ssh_comando



def cadastrar_servidor():

    #le o arquivo json
    banco = ler_banco()

    #cria um item
    servidor = {}
    servidor["hostname"] = raw_input("Digite o hostname: ")
    servidor["descricao"] = raw_input("Digite a descricao: ")


    #rotina de cricacao dos containers
    cmd = criar_container(servidor["hostname"])
    ssh_comando(cmd)

    cmd = pegar_ip_container(servidor["hostname"])
    ip = json.loads(ssh_comando(cmd))
    ip = ip[0].get("NetworkSettings").get("IPAddress")

    #adiciona o item criado na variavel que contem o json
    servidor["ip"] = ip
    banco["servidores"].append(servidor)

    #escreve a variavel do json, de volta no arquivoo
    escrever_banco(banco)
    print("Servidor "+ servidor["hostname"] + " cadastrado")



def listar_servidor():
    print("== Listar Servidor ==")

    banco = ler_banco()
    for i,u in enumerate(banco.get("servidores")):
        print "%s - %s - %s"%(i,u.get("hostname"),u.get("ip"))
    
    print __name__
    #raw_input("Presione enter para continuar")


def remover_servidor():
    print("== Remover Servidor ==")
    listar_servidor()

    id = input("Digite o ID que deseja remover: ")
    banco = ler_banco()

    #rotina de cricacao dos containers
    #{servidor:[{hostname:web1}]}    
    name = banco["servidores"][id]["hostname"]
    #print host    
    cmd = remover_container(name)
    ssh_comando(cmd)

    banco["servidores"].pop(id)

    escrever_banco(banco)        


def executar_comando_servidor():
    print("== SSH Servidor ==")
    listar_servidor()
    banco = ler_banco()

    id = input("Digite o ID do servidor: ")

    name = banco["servidores"][id]["hostname"]

    cmd  = raw_input("Digite o comando:")
    cmd = executar_comando(name, cmd)
    ssh_comando(cmd)


