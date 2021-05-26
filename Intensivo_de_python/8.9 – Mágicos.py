""": Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da
lista.
"""

magicos = ['Houdini', 'Fu-Manchu', 'Richiardi Jr', 'Jasper Maskelyne', 'Dai Vernon',
           'David Blaine', 'Siegfried Fischbacher', 'David Copperfield', 'Criss Angel', 'Penn e Teller',
           'Dynamo', 'Uri Geller', 'Nicolae Filipp Ladru', 'Tamariz', 'Jorge Blass', 'Inés – A Maga',
           'Paulino Gil', 'Yunke', 'Héctor Mancha', 'Howard Thurston', 'Lance Burton', 'Derren Brown']


def show_magicians(magic):
    for magico in magic:
        print(f'Nome do magico: {magico}')


show_magicians(magicos)
