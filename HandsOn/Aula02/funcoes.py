#!/usr/bin/python

usuarios = []


#Ao criar funcoes,
#Se o valor padrao for especificado, o argumento vira opcional
def cadastrar_usuario(nome, descricao=""):
    #utiliza a que esta no escopo global    
    global usuarios
    for u in usuarios: 
        if nome == u:
            print "Usuario ja cadastrado"
            break
    else:
        usuarios.append(nome)


    print "Cadastrado: ", nome
    print "Descricao: ", descricao
    return nome


#cadastrar_usuario("alex")
#cadastrar_usuario("alex","bonitao")


usuario1 = cadastrar_usuario("alex")
print usuarios

usuario2 = cadastrar_usuario("nunes")
print usuarios

usuario3 = cadastrar_usuario("alex")
print usuarios





