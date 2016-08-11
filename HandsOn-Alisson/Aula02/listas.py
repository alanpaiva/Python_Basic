#!/usr/bin/python

animais = ["gato","cachorro","tartaruga","papagaio","lagarto"]
mamiferos = []
aves = []
print "lista de aves: ",aves
aves.append("canario")
print "lista de aves: ",aves
print "total aves: ",len(aves)
animais.remove("papagaio")
print "lista de animais: ",animais
aves.insert(0,"papagaio")
print "lista de aves: ",aves
aves.pop(1)
print "lista de aves: ",aves
print "tartaruga esta no indice: ",animais.index("tartaruga")
animais.reverse()
print animais




