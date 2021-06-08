""" Faça uma lista de suas frutas favoritas e, então, escreva uma
série de instruções if independentes que verifiquem se determinadas frutas
estão em sua lista.
• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
• Escreva cinco instruções if. Cada instrução deve verificar se uma
determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma
frase, por exemplo, Você realmente gosta de bananas!
"""
favorite_fruits = ['maça','pera','uva', 'lixia', 'manga', 'caqui', 'abacate', 'amora', 'banana']

if 'maça' in favorite_fruits:
    print(f'Você realmente gosta de {favorite_fruits[0]}')
    
if 'caqui' in favorite_fruits:
    print(f'Você realmente gosta de {favorite_fruits[5]}')

if 'banana' in favorite_fruits:
    print(f'Você realmente gosta de {favorite_fruits[-1]}')
    
if 'amora' in favorite_fruits:
    print(f'Você realmente gosta de {favorite_fruits[7]}')
    
if 'manga' in favorite_fruits:
    print(f'Você realmente gosta de {favorite_fruits[4]}')