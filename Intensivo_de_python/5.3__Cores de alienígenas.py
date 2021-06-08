"""Suponha que um alienígena acabou de ser
atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
valor igual a 'green', 'yellow' ou 'red'.
• Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
mostre uma mensagem informando que o jogador acabou de ganhar cinco
pontos.
• Escreva uma versão desse programa em que o teste if passe e outro em que
ele falhe. (A versão que falha não terá nenhuma saída.) 5.4 – Cores de
alienígenas #2: Escolha uma cor para um alienígena, como foi feito no
Exercício 5.3, e escreva uma cadeia if-else.
• Se a cor do alienígena for verde, mostre uma frase informando que o jogador
acabou de ganhar cinco pontos por atingir o alienígena.
• Se a cor do alienígena não for verde, mostre uma frase informando que o
jogador acabou de ganhar dez pontos.
• Escreva uma versão desse programa que execute o bloco if e outro que
execute o bloco else.
"""

alien_color = 'green'

if alien_color == 'Green':
    print('O jogador acabou de ganhar cinco pontos. ')
    
alien_color = "red"

if alien_color == 'red':
    print('O Jogador acabou de perde 3 pontos. ')