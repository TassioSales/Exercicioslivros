""": Escolha uma cor para um alienígena, como foi feito no
Exercício 5.3, e escreva uma cadeia if-else.
• Se a cor do alienígena for verde, mostre uma frase informando que o jogador
acabou de ganhar cinco pontos por atingir o alienígena.
• Se a cor do alienígena não for verde, mostre uma frase informando que o
jogador acabou de ganhar dez pontos.
• Escreva uma versão desse programa que execute o bloco if e outro que
execute o bloco else."""

alien_color = 'Red'

if alien_color == 'green':
    print('O jogador acabou de ganhar cinco pontos por atingir o alienígena green')
elif alien_color != 'green':
    print(f'O jagador acabou de ganhar dez pontos por atingir o alienígena da cor {alien_color}')

alien_color = 'Blue'

if alien_color == 'green':
    print('O jogador acabou de ganhar cinco pontos por atingir o alienígena green')
else:
    print(f'O jagador acabou de ganhar dez pontos por atingir o alienígena da cor {alien_color}')    