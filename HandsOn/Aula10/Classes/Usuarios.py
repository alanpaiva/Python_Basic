#!/usr/bin/python

from model import session, Usuario as UsuarioModel

class Usuarios:
    id = 0
    login = ""
    senha = ""

    def cadastrar(self):
        self.login = raw_input("Digite o login do usuario: ")
        self.senha = raw_input("Digite a senha:")
        try:
            u = UsuarioModel(self)
            session.add(u)
            session.commit()
            print "Usuario cadastrado com sucesso!"
        except Exception as e:
            session.rollback()
            print "Falhou ao cadastrar usuario: ",e


    def listar(self):
        lista_usuario = session.query(UsuarioModel).all()    
        for usuario in lista_usuario:
            print "%s - %s"%(usuario.id,usuario.nome)

    def remover(self):
        self.listar()
        indice = input("Digite o id do usuario: ")
        try:
            usuario = session.query(UsuarioModel).filter_by(id=indice).first()
            session.delete(usuario)
            session.commit()
        except Exception as e:
            session.rollback()
            print "Falhou ao remover usuario: ",e






