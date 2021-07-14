# Escreva um programa que pergunte ao usuário
# quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
# oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
# contrário, informe que sua mesa está pronta.


qtdLugares = int(input('Ola seja bem vindo!!. Gostaria de uma mesa com quantos lugares ? '))

if qtdLugares >  8:
    print("No momentos estamos sem assentos para essa quantidade de pessoas.")
    print("Aguardade alguns instantes que ja provideciarei mesas para voces")
    
else:
    print("Temos uma mesa para voce venha comigo. ")