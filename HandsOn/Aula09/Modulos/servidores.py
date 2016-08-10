#!/usr/bin/python

from model import session, Servidor as ServidorModel #session cursor

def cadastrar_servidor(): #sempre chama o dicionario em funcao da funcao
    servidor = {} #dicionario recebe servidores/desc. vazio mesmo         
    servidor ["nome"] = raw_input("Digite o hostname do server: ")
    servidor ["descricao"] = raw_input("Digite descricao para o server: ")
    servidor ["ip"] = raw_input("Digite IP para o server: ")    

    try:
        s = ServidorModel()
        s.nome = servidor.get("nome")
        s.descricao = servidor.get("descricao")
        s.ip = servidor.get("ip")
        session.add(s)
        session.commit()
        print "Servidor cadastrado com sucesso!"
    except Exception as e:
        session.rollback()
        print "Falhou ao cadastrar servidor: ",e    

def listar_servidor():
    lista_servidor = session.query(ServidorModel).all()
    for servidor in lista_servidor:
        print "%s %s %s %s"%(servidor.id,servidor.nome,servidor.descricao,servidor.ip)

def remover_servidor():
    listar_servidor()
    indice = input("Digite o ID que deseja remover: ")
    result = session.query(ServidorModel).filter(ServidorModel.id==indice).first()
    session.delete(result)
    session.commit()
