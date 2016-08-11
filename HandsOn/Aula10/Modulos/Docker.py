#!/bin/python

from SSH import SSH

class Docker(SSH):
    def __init__(self):
        SSH.__init__()    

    def criar(self,name):
        comando="docker run -tdi --name %s --hostname %s ubuntu /bin/bash"%(name,name)
        return self.executar(comando)

    def remover(self,name):
        comando = "docker stop %s && docker rm %s"%(name,name)
        return self.executar_comando(comando)

    def pegar_ip(self,name):
        comando = "docker inspect %s"%name
        return self.executar_comando(comando)

    def executar_comando(self,name,cmd):
        comando = "docker exec %s bash -c '%s'"%(name,cmd)
        return self.executar_comando(comando)









