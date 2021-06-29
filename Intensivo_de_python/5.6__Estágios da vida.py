"""Escreva uma cadeia if-elif-else que determine o
123estágio da vida de uma pessoa. Defina um valor para a variável age e então: •
Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
que ela é um bebê.
• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma
mensagem dizendo que ela é uma criança.
• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma
mensagem dizendo que ela é um(a) garoto(a).
• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
mensagem dizendo que ela é um(a) adolescente.
• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
mensagem dizendo que ela é adulto.
• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
pessoa é idoso"""

age = 20

if 2 <= age < 4:
    print('Essa pessoa e um, BEBE')
elif 4 <= age < 13:
    print('Essa pessoa e um, GAROTO(A)')
elif 13 <= age < 20:
    print('Essa pessoa e um, ADOLESCENTE')
elif 20 <= age < 65:
    print('Essa pessoa e um, ADULTO')
else:
    print('Essa pessoa e um, IDOSO')