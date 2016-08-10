#!/usr/bin/python

class Usuario:
    id = 0
    #  _nome => protected  /  __nome => private
    _nome = ""   
    _senha = ""

    def cadastrar(self, nome, senha):
        self._nome = nome
        self._senha = senha

    def remover(self):
        print "Removendo usuario ", self.nome



if __name__ == "__main__":
    u = Usuario()
    u.cadastrar("Alex","teste")
    u.remover()





