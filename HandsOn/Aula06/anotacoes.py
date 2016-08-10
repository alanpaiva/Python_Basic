#!/usr/bin/python

1- dando permissao POSTGRE:
forlinux@developer  ~ $ sudo su - postgres
postgres@developer:~$ psql
psql (9.4.5)
Digite "help" para ajuda.
postgres-# \c loja2
Você está conectado agora ao banco de dados "loja2" como usuário "postgres".
loja2=# 
loja2=# grant ALL privileges on produtos to loja;
GRANT
loja2=# grant ALL privileges on produtos_id_seq to loja;
GRANT

2- dando permissao MYSQL:
forlinux@developer  ~ $ mysql -uroot -p123456
mysql> grant all privileges on loja2.* to loja@'%' identified by "4linux";
Query OK, 0 rows affected (0.00 sec)

limpar tabela:
mysql> truncate produtos;
Query OK, 0 rows affected (0.01 sec)

listar processos:
mysql> show processlist;
+----+------+-----------+-------+---------+------+-------+------------------+
| Id | User | Host      | db    | Command | Time | State | Info             |
+----+------+-----------+-------+---------+------+-------+------------------+
| 43 | root | localhost | loja2 | Query   |    0 | NULL  | show processlist |
+----+------+-----------+-------+---------+------+-------+------------------+
1 row in set (0.00 sec)


##########################################
############# SQL ALCHEMY ################
##########################################

pip install sqlalchemy

ORM - object relationship mapping

OpenStack utiliza o SQL ALCHEMY.


engine = create_engine("sqlite://banco.db")#estabelece conexão com o banco
Base = declarative_base()#executa as DDLs, reponsavel por criar estrutura

class Usuario(Base): #criando tabelas
    __tablename__ = 'usuario' #cria classe
    id = Column(Integer, primary_key=True) #id = primarykey
    nome = Column(String)
    senha = Column(String)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

Criando BANCO:
forlinux@developer  ~ $ cd 4520-Python/HandsOn/Aula07/
forlinux@developer  ~/4520-Python/HandsOn/Aula07 (master) $ sqlite3 banco.db
SQLite version 3.8.7.1 2014-10-29 13:59:56
Enter ".help" for usage hints.
sqlite> 

Mostrar tabelas:
sqlite> .tables

Ver schema da tabela:
sqlite> .schema usuario
CREATE TABLE usuario (
	id INTEGER NOT NULL, 
	nome VARCHAR, 
	senha VARCHAR, 
	PRIMARY KEY (id)
);

