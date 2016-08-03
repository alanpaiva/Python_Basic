#!/usr/bin/python

produtos = {"nome":"Celular",
             "preco": 988.97,
             "caracteristicas":["tela", "cor", "tamanho", "bateria"]}

#boas praticas:
#para pegar valor, usar o .get()
print produtos.get("nome")
#para alterar valor, usar []
print produtos["preco"]



produtos["nome"] = "Galaxy"
print produtos
print produtos.get("caracteristicas")
print produtos.get("caracteristicas")[3]


produtos["caracteristicas"][1] = "dimensoes"
print produtos

produtos["caracteristicas"].append("cor")
print produtos


#adicionar iten no dicionario: (se o item ja existir, sera atualizado)
produtos["nota"] = 4.8
print produtos


print produtos.keys()
print produtos.values()

#for para descobrir chave:valor
for k in produtos.keys():
    print "Chave: ", k
    print "valor: ", produtos.get(k)








