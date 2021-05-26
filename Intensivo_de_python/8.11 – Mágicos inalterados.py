"""Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico."""

magicos = ['Houdini', 'Fu-Manchu', 'Richiardi Jr', 'Jasper Maskelyne', 'Dai Vernon',
           'David Blaine', 'Siegfried Fischbacher', 'David Copperfield', 'Criss Angel', 'Penn e Teller',
           'Dynamo', 'Uri Geller', 'Nicolae Filipp Ladru', 'Tamariz', 'Jorge Blass', 'Inés – A Maga',
           'Paulino Gil', 'Yunke', 'Héctor Mancha', 'Howard Thurston', 'Lance Burton', 'Derren Brown']

magic_2 = magicos[:]


def show_magicians(magic):
    print(magic)


def make_great(magic):
    for i in range(len(magic)):
        magic[i] = 'O grande ' + magic[i]
        print(magic[i])


make_great(magicos)
show_magicians(magicos)
show_magicians(magic_2)