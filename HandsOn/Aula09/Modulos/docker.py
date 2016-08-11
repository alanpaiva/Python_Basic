#!/usr/bin/python


class Docker:
    def criar(self, name):
        return "docker run -tdi --name %s --hostname %s ubuntu /bin/bash"%(name,name)

    def remover(self, name):
        return "docker stop %s && docker rm %s"%(name,name) 

    def pegar_ip(self, name):
        return "docker inspect %s"%name

    def executar_comando(self, name, cmd):
        return "docker exec %s bash -c'%s'"%(name,cmd)
