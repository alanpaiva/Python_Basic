

from servidor import Servidor
from SSH import SSH


class Cloud(Servidor, SSH):
    pass


if __name__=="__main__":
    cloud = Cloud()

    cloud.acessar()

    cloud.contratar_cpu(1)
    cloud.contratar_memoria(512)
    cloud.contratar_disco(10)

    print cloud.cpu
    print cloud.memoria
    print cloud.disco



