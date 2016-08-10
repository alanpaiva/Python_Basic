#!/usr/bin/python

# define objeto de conexao com a base
from sqlalchemy import create_engine
# importa os metodos que criam a estrutura do banco
from sqlalchemy.ext.declarative import declarative_base
# importa os metodos para definir a estrutura do banco
from sqlalchemy import Column, Integer, String, ForeignKey
# importa o metodo para abrir uma sessao ( transaction )
from sqlalchemy.orm import sessionmaker, relationship #Abrir sessao:


#Para testar o banco, entrar no diretorio onde esta o banco.db
# >  sqlite3 banco.db
# > .tables    -Para listar as tabelas
# > .schema nome_tabela    -Para mostrar o schemaa


engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session =  sessionmaker()
Session.configure(bind=engine)
session = Session()



#nome de tabela sempre em minusculo
class Funcionario(Base):
    __tablename__ = "funcionario"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    dependente = relationship("Dependente")


class Dependente(Base):
    __tablename__="dependente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    #sempre usar "nometabela_id" para q o sqlalchemy reconheca
    funcionario_id = Column(Integer, ForeignKey("funcionario.id"))


if __name__ == "__main__":
    Base.metadata.create_all(engine)


    '''
    #cria instancia do funcionario
    antonio = Funcionario()
    antonio.nome = "Antoio"
    #cria instancia do dependente
    haroldo = Dependente()
    haroldo.nome = "Haroldo"
    #associa o dependente ao objeto pai
    antonio.dependente.append(haroldo)

    #grava dados no banco    
    session.add(antonio)
    session.add(haroldo)
    session.commit()
    '''

    '''
    #buscando funcionario
    funcionario = session.query(Funcionario).filter_by(id=1).first()
    
    #criando dependente
    dependente = Dependente()
    dependente.nome = "Maria"
    #vincula o dependente ao funcionario    
    funcionario.dependente.append(dependente)
    session.add(dependente)
    session.commit()
    #no sqlite:
    #sqlite> select * from dependente;
    #1|Haroldo|1
    #2|Maria|1

    '''

    

    '''
    #buscando funcionario
    # o .first() forca o python a trazer um unico objeto.
    # caso nao tenha o .first(), retornaria uma lista e seria
    # necessario usar um for, mesmo que so houvesse 1 resultado
    result = session.query(Funcionario, Dependente) \
                          .join(Dependente) \
                          .filter(Funcionario.id==1).first()
    
    print "Funcionario: ", result.Funcionario.nome
    for d in result.Funcionario.dependente:
        print "Dependente: ", d.nome


    '''


    result = session.query(Funcionario, Dependente) \
                          .join(Dependente) \
                          .filter(Funcionario.id==1).first()

    dependente = session.query(Dependente).filter_by(id=1).first()
    session.delete(dependente)
    session.commit()
    print "Funcionario: ", result.Funcionario.nome
    for d in result.Funcionario.dependente:
        print "Dependente: ", d.nome

    
