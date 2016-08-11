#!/usr/bin/python


class Servidor:
    nome=""
    descricao=""
    ip=""
    cpu=0
    memoria=0
    disco=0


    def __init__(self):
        self.cpu=1
        self.memoria=512
        self.disco = 50
   
    def contratar_cpu(self, cpu):
        self.cpu += cpu
        print "Total de CPUs: ", self.cpu

    def contratar_memoria(self, memoria):
        self.memoria += memoria
        print "Total de memoria: ", self.memoria, "Mb"

    def contratar_disco(self, disco):
        self.disco += disco
        print "Total de disco: ", self.disco, "Gb"
    

if __name__ == "__main__":
    servidor = Servidor()
    
    servidor.contratar_cpu(2)
    servidor.contratar_memoria(512)
    servidor.contratar_disco(10)
    
    print servidor.cpu
    print servidor.memoria
    print servidor.disco

