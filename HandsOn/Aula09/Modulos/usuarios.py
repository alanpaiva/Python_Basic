#!/usr/bin/python

from model import session, Usuario as UsuarioModel #session cursor

def cadastrar_usuario(): #sempre chama o dicionario em funcao da funcao
    usuario = {} #dicionario recebe user e pass. vazio mesmo         
    usuario ['login'] = raw_input("Digite o login do usuario: ")
    usuario ['senha'] = raw_input("Digite sua senha: ")

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
        print "%s -%s"%(usuario.id,usuario.nome)

def remover_usuario():
    listar_usuario()
    indice = input("Digite o ID que deseja remover: ")
    result = session.query(UsuarioModel).filter(UsuarioModel.id==indice).first()
    session.delete(result)
    session.commit()
