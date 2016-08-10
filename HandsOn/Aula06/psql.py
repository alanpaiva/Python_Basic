#!/usr/bin/python
#sudo apt-get install python-psycop2 -y -eh o conector com postgres

import psycopg2
try:
    con = psycopg2.connect("host=127.0.0.1 dbname=loja2 user=loja password=4linux")
    cursor = con.cursor()
#criar usuario:
#sudo su - postgres
#psql
#create user loja with password '4linux';
#alter database loja2 owner to loja;
#show databases dentro do postgres-# \l
#para conectar no banco \c loja2

    print "Conexao realizada com o banco"
    nome = "Sapato"
    descricao = "All star"
    preco = 80.99
    categoria = "calcado"
    cursor.execute("insert into produtos(nome,descricao,preco,categoria) values('%s','%s','%s','%s')"%(nome,descricao,preco,categoria)) #nao precisa do ";"
    con.commit() #se o commit der certo,     
    print "Produto cadastrado"
    cursor.execute("select * from produtos")
    result = cursor.fetchall()
    for r in result:
        print r
except Exception as e:
    con.rollback()
    print "Falhou ao conectar com o banco: ",e
finally:
    cursor.close()
    con.close()
    print "Conexao finalizada com o banco"
