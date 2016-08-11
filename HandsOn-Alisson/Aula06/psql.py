#!/usr/bin/python

import psycopg2
try:
    con = psycopg2.connect("host=127.0.0.1 dbname=loja2 user=loja password=4linux")
    cursor = con.cursor()
    print "Conexao realizada com o banco"
    nome = "Sapato"
    descricao = "All star"
    preco = 80.99
    categoria = "calcado"
    cursor.execute("insert into produtos(nome,descricao,preco,categoria) \
                   values('%s','%s',%s,'%s')"%(nome,descricao,preco,categoria))
    con.commit()
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







