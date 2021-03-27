"""4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
os números.
"""
lista = []
for c in range(1, 20, 2):
    print(c, end=" ")
    lista.append(c)
print(9 in lista)
