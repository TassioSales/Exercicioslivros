'''7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício
7.5 que faça o seguinte, pelo menos uma vez: • use um teste condicional na
instrução while para encerrar o laço; • use uma variável active para controlar
o tempo que o laço executará; • use uma instrução break para sair do laço
quando o usuário fornecer o valor 'quit'.
'''


while True:
    idade = int(input("Digite sua idade: "))
    if idade < 3:
        print('Ingresso Gratuito')
        break
    elif 3 <= idade < 12:
        print('O valor do se ingresso e de R$ 10.00')
        break
    elif 12 <= idade <= 20:
        print('O valor do ingresso e de R$ 15.00 ')
        break
    else:
        print('O valor do ingresso e de R$ 20.00')
        break
