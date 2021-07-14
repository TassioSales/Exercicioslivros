# Um cinema cobra preços diferentes para os
# ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
# de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
# ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
# dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
# informe-lhes o preço do ingresso do cinema.


while True:
    
    print('Digite quit para encerra o programa')
    idade = str(input("Digite sua idade: "))
    if idade == "quit":
        break

    idade = int(idade)
    
    if idade < 3:
        print("Seu ingresso e gratuito")
    elif idade > 3 and idade <= 12:
        print("Seu ingresso custa $10 dolares")
    elif idade > 12:
        print("Seu ingresso custa $15 dolares")
