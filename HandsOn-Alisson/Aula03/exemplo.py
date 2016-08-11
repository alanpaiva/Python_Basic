#!/usr/bin/python

def parametros_dinamicos(*args):
    print args[0]

parametros_dinamicos('alisson')
parametros_dinamicos('alisson','machado')
parametros_dinamicos('alisson','machado','de','menezes')

def exemplo_api(**kwargs):
    print kwargs.get("nome")

exemplo_api(nome='alisson')
exemplo_api(nome='alisson',sobrenome='machado de menezes')
