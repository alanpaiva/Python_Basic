#!/usr/bin/python

#instalar: sudo apt-get install python-mysqldb -y

import MySQLdb

try:
    con = MySQLdb.connect(host="127.0.0.1",
                          user="loja",
                          passwd="4linux",
                          db="loja2")
    print "Conexao realizada com sucesso!"
    cursor = con.cursor()
    nome = "Arduino"
    descricao = "Microcontrolador"
    preco = 59.99
    categoria = "Eletronicos"
    cursor.execute("insert into produtos(nome,descricao,preco,categoria) values ('%s','%s','%s','%s')"%(nome,descricao,preco,categoria))

    con.commit()
    print "Produto cadastrado com sucesso!"
#   cursor.execute("select * from produtos")
    cursor.execute("update produtos set nome='raspberry' where id=1")
    con.commit()
    print "Produto atualizado com sucesso!"
    result = cursor.fechall()
    for r in result:
        print r

except Exception as e:
    print "Falhou ao conectar com o banco: ",e
