#!/usr/bin/python


print("1 -  Cadastrar SysAdmin")
print("2 -  Listar SysAdmin")
print("3 -  Remover SysAdmin")
print("4 -  Cadastrar Servidor")
print("5 -  Listar Servidor")
print("6 -  Remover Servidor")


#opcao = int(raw_input("Digite a opcao desejada: "))
opcao = input("Digite a opcao desejada: ")


if opcao==1:
    print("Chamar a funcao Cadastra SysAdmin")
elif opcao==2:
    print("Chamar a funcao Listar SysAdmin")
elif opcao==3:
    print("Chamar a funcao Remover SysAdmin")
elif opcao==4:
    print("Chamar a funcao Cadastra Servidor")
elif opcao==5:
    print("Chamar a funcao Listar Servidor")
elif opcao==6:
    print("Chamar a funcao Remover Servidor")
else:
    print("Opcao invalida!")




