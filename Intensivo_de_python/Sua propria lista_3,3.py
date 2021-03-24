"""Pense em seu meio de transporte preferido, como
motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter
uma moto Honda”"""

motosECarros = ["Kwid", "CBX 300", "Siena", 'Blazer']

print(f'Ja quero um {motosECarros[0]}')
print(f'Vou comprar uma {motosECarros[1]}')
print(f'Modinha do momento e o {motosECarros[2]}')
print(f'Carrão de todos os tempos {motosECarros[3]}')

print("\n")

for itens in motosECarros:
    if itens == 'Kwid':
        print(f'Ja quero um {itens}')
    if itens == 'CBX 300':
        print(f'Vou comprar uma {itens}')
    if itens == 'Siena':
        print(f'Modinha do momento e o {itens}')
    if itens == 'Blazer':
        print(f'Carrão de todos os tempos {itens}')
