#!/usr/bin/python

from pymongo import MongoClient

client = MongoClient("127.0.0.1")
db = client["curso_python"]

aula = {"aula":"sqlalchemy"}
db.aulas.update({"nome":"python"},
                {"$addToSet":{"aulas":aula}})

db.aulas.update({"nome":"python"},
                {"$pull":{"aulas":{"aula":"basico"}}})
