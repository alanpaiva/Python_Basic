#!/usr/bin/pythonn

def parametros_dinamicos(*args):
    print args


parametros_dinamicos("alex")
parametros_dinamicos("alex", "teste")
parametros_dinamicos("alex", "teste", "teste 2")


def exemplo_api(**kwargs):
    #print kwargs
    print kwargs.get("nome")


exemplo_api(nome="Alex")
exemplo_api(nome="Alex", sobrenome="Nunes")

