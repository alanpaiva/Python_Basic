#!/usr/bin/python

#Contante sempre em MAIUSCULAS
PI = 3.14

numero=1

dolar=3.23

texto = "Curso de Python"

dicionario={"Dinossauro":"animal pre-historico",
            "Cebola":"Cebola eh um tempero",
            "4Linux":3057,
            "produtos":["tenis","sapato","sandalia"]}

#Listas
notas=[5, 6.5, 7, 10, 9.5]
materias=["Portugues", "Matematica", "Historia", "Geografia", "Artes"]

tupla=["param1", "param2", "param3"]

#zip() junta duas listas
print "Historico do aluno"
print zip(materias, notas)

#Pegar itens do dicionario
print "=================="
print dicionario.get("produtos")


#Pegar itens de uma tupla
print "=================="
print "Valor 0 da tupla: ", tupla[0]


print "ASPAS \""


