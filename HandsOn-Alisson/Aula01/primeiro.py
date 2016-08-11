#!/usr/bin/python
#
# Feito por: Alisson Machado
# Data: 01/08/2016
# Email: alisson.machado@4linux.com.br
#

"""
 O  objeto desse script e fazer a autenticao dos usuarios do sistema
 o script tambem faz integracao com mysql e postgresql
"""



print "== Sistema de Autenticacao =="
print "Digite o seu usuario: "
usuario = raw_input()
senha = raw_input("Digite a sua senha: ")
print "Autenticando o usuario: "+usuario
if senha == "4linux":
    print "Autenticado com sucesso"
else:
    print "Falhou ao autenticar"
