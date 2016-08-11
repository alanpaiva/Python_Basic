
from servidor import Servidor
from IPMI import IPMI


class Fisico(Servidor, IPMI):

    slot_ocupado=1
    slot_memoria=4

    slot_disco=4
    slot_disco_ocupado = 1


    def __init__(self,cpu=1, memoria=1024, disco=512):
        self.cpu = cpu
        self.memoria = memoria
        self.disco = disco

    def contratar_memoria(self, memoria):
        if self.slot_ocupado < self.slot_memoria:
            self.memoria += memoria
            self.slot_ocupado += 1
            print "Total de memoria: ", self.memoria, "Mb"
        else:
            print "Nao ha slots de memoria disponiveis"

    def contratar_cpu(self, cpu):
        print "Faca  um upgrade de maquina"

    def contratar_disco(self, disco):
        if self.slot_disco_ocupado < self.slot_disco:
            self.disco += disco
            self.slot_disco_ocupado += 1
            print "Total de disco: ", self.disco, "Gb"
        else:
            print "Nao ha slots de disco disponiveis"





if __name__=="__main__":
    fisico = Fisico()
    
    fisico.acessar()

    fisico.contratar_cpu(3)
    fisico.contratar_memoria(1024)
    fisico.contratar_disco(50)





