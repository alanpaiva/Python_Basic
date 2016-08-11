#!/usr/bin/python
#
# apt-get install python-mysqldb
#

import MySQLdb

try:
    con = MySQLdb.connect(host="127.0.0.1",
                          user="loja",
                          passwd="4linux",db="loja2")
    print "Conexao realizada com sucesso!"
    cursor = con.cursor()
    nome = "Arduino"
    descricao = "Microcontrolador"
    preco = 59.99
    categoria = "eletronicos"
    cursor.execute("insert into produtos(nome,descricao,preco,categoria) \
                   values('%s','%s',%s,'%s')"%(nome,descricao,preco,categoria))
    con.commit()    
    print "Produto cadastrado com sucesso!"
    cursor.execute("update produtos set nome='raspberry' where id=1")
    con.commit()
    print "produto atualizado com sucesso!"
    cursor.execute("select * from produtos")
    result = cursor.fetchall()
    for r in result:
        print r


except Exception as e:
    print "Falhou ao conectar com o banco: ",e
