#!/usr/bin/python

#pip install pymongo

from pymongo import MongoClient

client = MongoClient("127.0.0.1")
db =  client["curso_python"]

#insert
#db.aulas.insert({"curso":"mongodb", "assunto":"replicacao", "aula":5})

#update na collection
#db.aulas.update({"curso":"mongodb"}, {"$set":{"assunto":"backup"}})

#remover dados
#db.aulas.remove({"curso":"cassandra"})

# para remover todos os dados:
#db.aulas.remove()


#select na collection aula
#aulas = db.aulas.find()
#for a in aulas:
#    print a.get("curso"), a.get("assunto")

'''
cursos = {"nome":"python", "aulas":[
                                       {"aula":"basico"},
                                       {"aula":"estrutura de decisao"},
                                       {"aula":"funcoes"}
                                   ]}

db.aulas.insert(cursos)
'''

aula = {"aula":"sqlalchemy"}
#db.aulas.update({"nome":"python"},{"$addToSet":{"aulas":aula}})


#para remover um item da lista, usamos o $pull
db.aulas.update({"nome":"python"},{"$pull":{"aulas":{"aula":"basico"}}})



