#!/usr/bin/python

print("==Sistema de Autoescola==")

nome = raw_input("Digite seu nome: ")
idade =input("Digite sua idade: ")


if idade>=18:
    print("Cliente cadastrado")
else:
    responsavel = raw_input("Esta acompanhado do responsavel: ")
    if responsavel[0].lower() in "sim":
        nome_responsavel = raw_input("Digite o nome do responsavel: ")
        print("Cliente cadastrado")
    else:
        print("Nao eh possivel efetuar o cadastro")

