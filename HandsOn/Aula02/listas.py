#!/usr/bin/python

animais = ["gato", "cachorro", "tartaruga", "papagaio", "lagarto"]
mamiferos = []
aves = []

print "Lista de Aves", aves

#adicionar itens em uma lista
aves.append("canario")
print "Lista de Aves", aves

#pega tamanho da lista
print "total de aves: ", len(aves)

#remover itens de uma lista
animais.remove("papagaio")
print "Lista de animais: ", animais

#incluir item em determinada posicao:
aves.insert(0,"papagaio")
print "Lista de Aves", aves

#remover item especifico pelo index
#POP() sem parametro, remove o ultimo item da lista
aves.pop(1)
print "Lista de Aves", aves

print "tartaruga esta no indice ", animais.index("tartaruga")

#inverter lista
animais.reverse()
print animais


