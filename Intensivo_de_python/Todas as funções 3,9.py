"""Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função apresentada
neste capítulo pelo menos uma vez.
"""

lista = [5,20,45,80,15,65,2,47,10,16,12,14,78,54,63,65,45,41,100,65,145]
print(lista)
lista.pop(5)
print(lista)
lista[5] = 68
print(lista)
del lista[0]
print(lista)
lista[0] = 7
print(lista)

print(sorted(lista))
print(sorted(lista, reverse=True))



lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

print(len(lista))

lista.remove(10)
print(lista)
