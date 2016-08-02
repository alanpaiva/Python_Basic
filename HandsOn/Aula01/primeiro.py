#!/usr/bin/python
#
# Feito por Alexander Nunes
# Data: 01/08/2016
# Email: alexandercn@hottmail.com
#
'''
Script Dummy
O Objetivo desse script e simular autenticacao de usuarios
Esse tipo de comentario eh utilizado para documentacao como em https://readthedocs.org/

'''

print "== Sistema de autenticacao =="
print "Digite seu usuario: "
usuario = raw_input()
senha = raw_input("Digite a sua senha: ")


print "Autenticando usuario: " + usuario
#"," tambem funciona para concatenar (Utilizar para numeross). Ex.:
#print "Autenticando usuario: ", usuario 

if senha == "4linux":
    print "Autenticado com sucesso"
else:
    print "Falhou ao autenticar"





