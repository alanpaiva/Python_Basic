#!/bin/python

def criar_container(name):
    return "docker run -tdi --name %s --hostname %s ubuntu /bin/bash"%(name,name)
                     # web1
def remover_container(name):
                        #web1           web1
    return "docker stop %s && docker rm %s"%(name,name)

def pegar_ip_container(name):
    return "docker inspect %s"%name

def executar_comando(name,cmd):
    return "docker exec %s bash -c '%s'"%(name,cmd)









