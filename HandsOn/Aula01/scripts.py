#!/usr/bin/python

#Estear Eggg!!
#>>>import this


nome = "Guido Van Rossum"
idade = 59

print "O criador do Python se chama " + nome
print "A idade dele  eh ", idade, " anos"

print "O criador do Python eh %s e sua idade  eh %d" %(nome, idade)
# %s tambem funciona para decimais
#print "O criador do Python eh %s e sua idade  eh %s" %(nome, idade)


print "select %s, %s, %s from produtos" %("Coluna1","Coluna2","Coluna3")

# raw_input serve para capturar strings (input de numeros viram string)
nome = raw_input("Digite o seu nome: ")
#input() serve apenas para capturar numeros
idade = input("Digite sua idade: ") 



