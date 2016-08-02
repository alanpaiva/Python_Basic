#!/usr/bin/python

#Por exemplo: usuario = arthur.dent senha = mochileiro

nome = raw_input("Digite seu login: ")
senha = raw_input("Digite sua senha: ")


if nome=="arthur.dent" and senha=="mochileiro":
    print "Seja Bem Vindo %s" %(nome)
else:
    print "Acesso Negado"


