#!/usr/bin/python

from Modulos.Docker import criar_container, remover_container, executar_comando, pegar_ip_container
from Modulos.SSH import executa_comando as ssh_comando
from model import session, Servidor as ServidorModel

def cadastrar_servidor():
    servidor = {}
    servidor["hostname"] = raw_input("Digite o nome do servidor:")
    servidor["descricao"] = raw_input("Digite uma descricao: ")
    try:
        s = ServidorModel()
        s.nome = servidor.get("hostname")
        s.descricao = servidor.get("descricao")
        session.add(s)
        session.commit()
    except Exception as e:
        session.rollback()
        print "Falhou ao cadastrar servidor: ",e    

    # rotina de criacao dos containers
    #cmd = criar_container(servidor["hostname"])
    #ssh_comando(cmd)
    #cmd = pegar_ip_container(servidor["hostname"])
    #ip = ssh_comando(cmd)
    #ip = json.loads(ip)
    #ip = ip[0].get("NetworkSettings").get("IPAddress")
    #servidor["ip"] = ip # nginx
    #banco["servidores"].append(servidor)


def listar_servidor():
    servidores = session.query(ServidorModel).all()
    for servidor in servidores:
        print "%s - %s - %s"%(servidor.id,servidor.nome,servidor.descricao)

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
    
    try:
        servidor = session.query(ServidorModel) \
                          .filter_by(id=servidor_id).first()
        session.delete(servidor)
        session.commit()
        print "Servidor removido com sucesso!"
    except Exception as e:
        session.rollback()
        print "Falhou ao remover servidor: ",e   

    #cmd = remover_container(name)
    # cmd = docker stop web1 && docker rm web1
    #ssh_comando(cmd)






