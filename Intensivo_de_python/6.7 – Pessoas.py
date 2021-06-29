"""Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista
de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
você sabe sobre cada pessoa."""

pessoa = {"nome":'Tassio', 'sobrenome':'Sales', 'idade':'31', 'cidade de residencia': 'Pedregal'}
pessoa_1 = {"nome":'Julia', 'sobrenome':'Santos', 'idade':'23', 'cidade de residencia': 'Gama'}
pessoa_2 = {"nome":'Jhon', 'sobrenome':'preslei', 'idade':'27', 'cidade de residencia': 'Pedregal'}

peoples = [pessoa, pessoa_1, pessoa_2]

for people in peoples:
    nome_completo = people['nome'] + ' ' + people['sobrenome']
    print(nome_completo)
    print("\t Sua idade e " + people['idade'])
    print("\t Voce mora em "+ people['cidade de residencia'])
    print('\n')