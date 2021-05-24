""" Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
informe-lhes o preço do ingresso do cinema."""


while True:
    idade = int(input("Digite sua idade: "))
    if idade < 3:
        print('Ingresso Gratuito')
    elif 3 <= idade < 12:
        print('O valor do se ingresso e de R$ 10.00')
    elif 12 <= idade <= 20:
        print('O valor do ingresso e de R$ 15.00 ')
    else:
        print('O valor do ingresso e de R$ 20.00')
