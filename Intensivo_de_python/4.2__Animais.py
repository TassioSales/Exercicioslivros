"""Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses
animais têm em comum. Você poderia exibir uma frase como Qualquer um
desses animais seria um ótimo animal de estimação!"""


animais = ['Papagaio', 'Cachorro', 'Gato', 'Calopsita']

for animal in animais:
    if animal == "Papagaio":
        print(f"O {animal} fala demais")
    elif animal =='Cachorro':
        print(f"O {animal} e o mais amoroso")
    elif animal == 'Gato':
        print(f"O {animal} e o mais independente")
    elif animal == 'Calopsita':
        print(f"O {animal}  canta muito")      