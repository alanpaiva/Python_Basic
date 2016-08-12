#!/usr/bin/python

from Modulos.Docker import Docker
from model import session, Servidor as ServidorModel
import json

class Servidores:
    id = 0
    nome = ""
    descricao = ""
    ip = ""

    def cadastrar(self):
        self.nome = raw_input("Digite o nome do servidor:")
        self.descricao = raw_input("Digite uma descricao: ")
        try:
            # instancia dos objetos Docker
            docker = Docker()
            docker.criar(self.nome)
            container = docker.pegar_ip(self.nome)
            container = json.loads(container)
            self.ip = container[0].get("NetworkSettings").get("IPAddress")
            s = ServidorModel(self)
            session.add(s)
            session.commit()
        except Exception as e:
            session.rollback()
            print "Falhou ao cadastrar servidor: ",e            


    def listar(self):
        servidores = session.query(ServidorModel).all()
        for servidor in servidores:
            print "%s - %s - %s -%s"%(servidor.id,
                                      servidor.nome,
                                      servidor.ip,
                                      servidor.descricao)

    def exec_comando_servidor(self):
        self.listar()
        servidor_id  = input("Digite o id do servidor: ")
        servidor = session.query(ServidorModel).filter_by(id=servidor_id).first()
        cmd = raw_input("Digite o comando a ser executado: ")

        #cmd = executar_comando(name,cmd)
        docker = Docker()
        print docker.shell(servidor.nome, cmd)


    def remover(self):
        docker = Docker()
        self.listar()
        servidor_id  = input("Digite o id do servidor: ")


        try:
            servidor = session.query(ServidorModel) \
                              .filter_by(id=servidor_id).first()
            docker.remover(servidor.nome)

            session.delete(servidor)
            session.commit()
            print "Servidor removido com sucesso!"
        except Exception as e:
            session.rollback()
            print "Falhou ao remover servidor: ",e   

        #cmd = remover_container(name)
        # cmd = docker stop web1 && docker rm web1
        #ssh_comando(cmd)






