#!/usr/bin/python

import json
from Modulos.docker import Docker
from Modulos.SSH import SSH
from model import session, Servidor as ServidorModel #session cursor


class Servidor:
    id = 0
    nome = ""
    descricao = ""
    ip = ""

    def cadastrar(self): #sempre chama o dicionario em funcao da funcao

        self.nome = raw_input("Digite o hostname do server: ")
        self.descricao = raw_input("Digite descricao para o server: ")
        #self.ip = raw_input("Digite IP para o server: ")    

        try:
            ssh = SSH()
            docker = Docker()
            
            ssh.executa_comando(docker.criar(self.nome))

            
            container = ssh.executa_comando(docker.pegar_ip(self.nome))
            container = json.loads(container)

            self.ip = container[0].get("NetworkSettings").get("IPAddress")

            s = ServidorModel(self)
            #s.nome = servidor.get("nome")
            #s.descricao = servidor.get("descricao")
            #s.ip = servidor.get("ip")
            
            session.add(s)
            session.commit()
            print "Servidor cadastrado com sucesso!"
        except Exception as e:
            session.rollback()
            print "Falhou ao cadastrar servidor: ",e    

    def listar(self):
        lista_servidor = session.query(ServidorModel).all()
        for servidor in lista_servidor:
            print "%s %s %s %s"%(servidor.id,servidor.nome,servidor.descricao,servidor.ip)

    def remover(self):
        self.listar()
        indice = input("Digite o ID que deseja remover: ")
        result = session.query(ServidorModel).filter(ServidorModel.id==indice).first()
        session.delete(result)
        session.commit()
