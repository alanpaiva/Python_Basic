#!/usr/bin/python

idade = 17
pais = True


if idade>=18:
    print("Pode tirar habilitacao")
elif pais==True:
    print("Pode tirar habilitacao")
else:
    print("Nao tem idade suficiente")



for x in range(0,10):
    print x




#ELSE pode ser usado no FOR, para o caso de nao encontrar o produto
produtos =  ["camiseta", "tenis", "calca", "bermuda", "bone"]
for p in produtos:
    if p=="bermudasdf":
        print p+" encontrada"
        break
else:
    print "produto nao encontrado"



#CONTINUE pode ser usado para tratar uma  excecao. Retirar o "h":
for letra in "python":
    if letra=="h":
        print "encontrado"
        continue
    else:
        print letra
    print "testando continue"

