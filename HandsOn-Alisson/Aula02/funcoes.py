#!/usr/bin/python

usuarios = []

def cadastrar_usuario(nome,descricao=""):
    global usuarios    
    for u in usuarios:
        if u == nome:
            print "Usuario ja cadastrado"
            break
    else:
        usuarios.append(nome)
    
    print "Cadastrado usuario: "+nome
    print "Descricao: "+descricao
    return nome

usuario1 = cadastrar_usuario("Alisson")
usuario2 = cadastrar_usuario("Rafael")
usuario3 = cadastrar_usuario("Rafael")
print usuarios






