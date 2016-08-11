#!/usr/bin/python

from model import session, Usuario as UsuarioModel

def cadastrar_usuario():
    usuario = {}
    usuario['login'] = raw_input("Digite o login do usuario: ")
    usuario['senha'] = raw_input("Digite a senha:")
    try:
        u = UsuarioModel()
        u.nome = usuario.get("login")
        u.senha = usuario.get("senha")
        session.add(u)
        session.commit()
        print "Usuario cadastrado com sucesso!"
    except Exception as e:
        session.rollback()
        print "Falhou ao cadastrar usuario: ",e


def listar_usuario():
    lista_usuario = session.query(UsuarioModel).all()    
    for usuario in lista_usuario:
        print "%s - %s"%(usuario.id,usuario.nome)

def remover_usuario():
    listar_usuario()
    indice = input("Digite o id do usuario: ")
    try:
        usuario = session.query(UsuarioModel).filter_by(id=indice).first()
        session.delete(usuario)
        session.commit()
    except Exception as e:
        session.rollback()
        print "Falhou ao remover usuario: ",e

if __name__ == '__main__':
    print __name__
    cadastrar_usuario()








