#!/usr/bin/python

from Modulos.Usuarios import ler_banco, escrever_banco
from Modulos.Docker import criar_container, remover_container, executar_comando, pegar_ip_container
from Modulos.SSH import executa_comando as ssh_comando
import json

def cadastrar_servidor():
    banco = ler_banco()
    servidor = {}
    servidor["hostname"] = raw_input("Digite o nome do servidor:")
    servidor["descricao"] = raw_input("Digite uma descricao: ")

    # rotina de criacao dos containers
    cmd = criar_container(servidor["hostname"])
    ssh_comando(cmd)
    cmd = pegar_ip_container(servidor["hostname"])
    ip = ssh_comando(cmd)
    ip = json.loads(ip)
    ip = ip[0].get("NetworkSettings").get("IPAddress")
    servidor["ip"] = ip # nginx
    banco["servidores"].append(servidor)
    escrever_banco(banco)

def listar_servidor():
    banco = ler_banco()
    for indice,servidor in enumerate(banco.get("servidores")):
        print "%s - %s - %s"%(indice,servidor.get("hostname"),
                              servidor.get("ip"))
def exec_comando_servidor():
    listar_servidor()
    banco = ler_banco()
    servidor_id  = input("Digite o id do servidor: ")
    name = banco["servidores"][servidor_id]["hostname"]
    cmd = raw_input("Digite o comando a ser executado: ")
    cmd = executar_comando(name,cmd)
    ssh_comando(cmd)

def remover_servidor():
    listar_servidor()
    servidor_id  = input("Digite o id do servidor: ")
    banco = ler_banco()
    name = banco["servidores"][servidor_id]["hostname"]
    # name = web1
    cmd = remover_container(name)
    # cmd = docker stop web1 && docker rm web1
    ssh_comando(cmd)
    banco["servidores"].pop(servidor_id)
    escrever_banco(banco)






