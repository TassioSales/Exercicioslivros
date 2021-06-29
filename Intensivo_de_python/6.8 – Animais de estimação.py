"""Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
fizer isso, apresente tudo que você sabe sobre cada animal de estimação.
"""

mila = {'nome_pet': 'mila', "dono": "Rodrigo", "tipo": 'Cachorro', "porte": 'medio'}
noki = {'nome_pet': 'noki', "dono": "Pablo", "tipo": 'Cachorro', "porte": 'medio'}
swam = {'nome_pet': 'swam', "dono": "Iago", "tipo": 'Cachorro', "porte": 'grande'}
dandara = {'nome_pet': 'dandara', "dono": "Tassio Sales", "tipo": 'Cachorro', "porte": 'medio'}
dani = {'nome_pet': 'dani', "dono": "Julia Santos", "tipo": 'Cachorro', "porte": 'medio'}
negao = {'nome_pet': 'negao', "dono": "Tony Sales", "tipo": 'Cachorro', "porte": 'grande'}
taigo = {'nome_pet': 'taigo', "dono": 'Celio Mendonça', "tipo": 'Cachorro', "porte": 'pequeno'}

pets = [mila, noki, swam, dandara, dani, negao, taigo]

for nome_pet in pets:
    print('Dono: ' + nome_pet['dono'])
    print('\t' +'NOME: '+nome_pet['nome_pet'].title())
    print('\t' +'Tipo: '+ nome_pet['tipo'].title())
    print('\t' +'Porte: '+nome_pet['porte'].title())
    print('\n')