#!/usr/bin/python

print "-= Sistema Autoescola =-"
nome = raw_input("Digite o seu nome")
idade = input("Digite a sua idade")

if int(idade) >= 18:
    print "Cliente cadastrado"
else:
    responsavel = raw_input("Esta acompanhado de responsavel?")
    if responsavel[0].lower() in "sim":
        nome_responsavel = raw_input("Digite o nome do responsavel:")
        print "Cliente cadastrado"
    else:
        print "Nao e possivel efetuar o cadastro"



