"""Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário.
"""
pessoa = {}

pessoa["Nome"] = str(input('Digite seu primeiro nome: '))
pessoa['Sobrenome'] = str(input('Digite seu sobre nome: '))
pessoa['Idade'] = int(input('Digite sau idade: '))
pessoa['Cidade de residencia'] = str(input('Digite o nome da cidade onde reside: '))
print(pessoa)