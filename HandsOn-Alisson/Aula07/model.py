#!/usr/bin/python
# define o objeto de conexao com a base
from sqlalchemy import create_engine
# import os metodos que criam a estrura do banco
from sqlalchemy.ext.declarative import declarative_base
# importa os metodos para definir a estrutura do banco
from sqlalchemy import Column, Integer, String, Table, ForeignKey,DateTime
# importa o metodo para abrir uma sessao( transaction )
from sqlalchemy.orm import sessionmaker, relationship
from random import randint
from datetime import datetime

# linha que conecta com o banco
engine = create_engine("mysql://loja:4linux@localhost/loja2")
# instancia do objeto para criar a estrutura do banco
Base = declarative_base()
# cria objeto sessionmaker
Session = sessionmaker()
# define em qual banco deve abrir a sessao
Session.configure(bind=engine)
# abre sessao ( define o cursor )
session = Session()

usuario_servidor = Table('usuario_servidor',
                          Base.metadata,
                       Column('usuario_id',Integer,ForeignKey('usuario.id')),
                       Column('servidor_id',Integer,ForeignKey('servidor.id'))
                        )

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    senha = Column(String(255))
    servidor = relationship("Servidor",secondary=usuario_servidor)
    token = relationship("Token")

class Servidor(Base):
    __tablename__ = 'servidor'
    id = Column(Integer,primary_key=True)
    nome = Column(String(255))
    descricao = Column(String(255))
    ip = Column(String(255))

class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id"))
    servidor_id = Column(Integer,ForeignKey("servidor.id"))
    token = Column(String(255),default=str(randint(1000,9999)))
    motivo = Column(String(255),nullable=False)
    data = Column(DateTime,default=datetime.now())
    servidor = relationship("Servidor")
    usuario = relationship("Usuario")


if __name__ == '__main__':
    # cria estrutura do banco
    Base.metadata.create_all(engine)
    novo_token = Token()
    novo_token.motivo = "Atualizado de seguranca do servidor"
    usuario = session.query(Usuario).filter_by(id=3).first()
    usuario.token.append(novo_token)
    servidor = session.query(Servidor).filter_by(id=1).first()
    novo_token.servidor = servidor
    session.add(novo_token)
    session.commit()






 
