""": Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função apresentada
neste capítulo pelo menos uma vez."""

lista = ['99', '27', '154', '13', '15', '43', '2', '32', '56', '45', '24', '12', '8', '6', '4', '3', '1']
print(lista)
lista.remove('99')
print(lista)
lista.append('999')
print(lista)
del lista[1]
print(lista)
lista.pop()
print(lista)
lista.append('23')
print(lista)
print(sorted(lista))
print(sorted(lista, reverse=True))
lista.sort()
print(lista)




