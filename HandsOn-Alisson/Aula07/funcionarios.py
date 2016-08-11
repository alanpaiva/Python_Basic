#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Funcionario(Base):
    __tablename__ = 'funcionario'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    dependente = relationship("Dependente")

class Dependente(Base):
    __tablename__ = "dependente"
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    funcionario_id = Column(Integer,ForeignKey("funcionario.id"))

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # Buscando funcionario
    result = session.query(Funcionario,Dependente) \
                         .join(Dependente) \
                         .filter(Funcionario.id==1).first()
    dependente = session.query(Dependente).filter_by(id=1).first()
    session.delete(dependente)
    session.commit()
    print "Funcionario: ",result.Funcionario.nome
    for d in result.Funcionario.dependente:
        print "Dependente: ",d.nome
    











