""" Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve
estar personalizada com o nome da pessoa.
"""

nomeAmigo = ['Pedro', 'Thiagol', 'Robson', 'Fillipe', 'Jhon presley', 'Ruan']

print(f'E um prazer te conhecer {nomeAmigo[0]}')
print(f'Obrigado pela ajuda {nomeAmigo[1]}')
print(f'Seja bem vindo {nomeAmigo[2]}')
print(f'So podia ser o nerd do {nomeAmigo[3]}')
print(f'Cara eu nao te tanko {nomeAmigo[4]}')
print(f'Infelizemente nao sei quem e voce {nomeAmigo[5]}')

print('\n')

for itens in nomeAmigo:
    if itens == 'Pedro':
        print(f'E um prazer te conhecer {itens}')
    elif itens == 'Thiagol':
        print(f'Obrigado pela ajuda {itens}')
    elif itens == 'Robson':
        print(f'Seja bem vindo {nomeAmigo[2]}')
    elif itens == 'Fillipe':
        print(f'So podia ser o nerd do {nomeAmigo[3]}')
    elif itens == 'Jhon presley':
        print(f'Cara eu nao te tanko {nomeAmigo[4]}')
    elif itens == 'Ruan':
        print(f'Infelizemente nao sei quem e voce {nomeAmigo[5]}')

