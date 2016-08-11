#!/usr/bin/python

produtos = {"nome":"Celular",
            "preco":998.97,
            "caracteristicas":["tela","cor","tamanho","bateria"]}

print produtos.get("nome")
print produtos["preco"]

produto["nome"] = "Galaxy J5"
print produtos
print produtos.get("caracteristicas")
print produtos.get("caracteristicas")[3]
produtos["caracteristicas"][1] = "dimensoes"
produtos["caracteristicas"].append("cor")
print produtos
produtos["nota"] = 4.8
print produtos.keys()
print produtos.values()
for k in produtos.keys():
    print "Chave: ",k
    print "valor: ",produtos.get(k)














