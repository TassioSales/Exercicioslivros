"""Comece com uma cópia de seu programa do
Exercício 8.9. Escreva uma função chamada make_great() que modifique a
lista de mágicos acrescentando a expressão o Grande ao nome de cada
mágico. Chame show_magicians() para ver se a lista foi realmente modificada."""

magicos = ['Houdini', 'Fu-Manchu', 'Richiardi Jr', 'Jasper Maskelyne', 'Dai Vernon',
           'David Blaine', 'Siegfried Fischbacher', 'David Copperfield', 'Criss Angel', 'Penn e Teller',
           'Dynamo', 'Uri Geller', 'Nicolae Filipp Ladru', 'Tamariz', 'Jorge Blass', 'Inés – A Maga',
           'Paulino Gil', 'Yunke', 'Héctor Mancha', 'Howard Thurston', 'Lance Burton', 'Derren Brown']


def show_magicians(magic):
    print(magic)


def make_great(magic):
    for i in range(len(magic)):
        magic[i] = 'O grande ' + magic[i]
        print(magic[i])


make_great(magicos)
show_magicians(magicos)

