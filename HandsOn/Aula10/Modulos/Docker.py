#!/bin/python

#comando para apagar todos os dockers criados
# docker rm -f $(docker ps -a)



from SSH import SSH

class Docker(SSH):
    def __init__(self):
        SSH.__init__(self)    

    def criar(self,name):
        comando="docker run -tdi --name %s --hostname %s ubuntu /bin/bash"%(name,name)
        return self.executar_comando(comando)

    def remover(self,name):
        comando = "docker stop %s && docker rm %s"%(name,name)
        print comando
        return self.executar_comando(comando)

    def pegar_ip(self,name):
        comando = "docker inspect %s"%name
        return self.executar_comando(comando)

    def shell(self,name,cmd):
        comando = "docker exec %s bash -c '%s'"%(name,cmd)
        return self.executar_comando(comando)










