#!/usr/bin/python

idade = 18
pais = True

if idade >= 18:
    print "Pode tirar habilitacao"
elif pais == True:
    print "Pode tirar habilitacao"
else:
    print "Nao tem idade suficiente"

for x in range(0,10):
    print x

produtos = ["camiseta","tenis","calca","bermuda","chapeu"]
for p in produtos:
    if "bermuda" == p:
        print p+" encontrada"
        break
else:
    print "Produto nao encontrado"

for letra in "python":
    if letra == "h":
        print letra+" encontrada"
        continue
    else:
        print letra
    print "Testando a instrucao continue"


















