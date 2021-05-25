"""Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades
diferentes em que pelo menos uma delas não esteja no país default."""


def describe_city(nomeCity, pais='Brasil'):
    """

    :param nomeCity: Recebe o nome de uma cidade
    :param pais: Recebe o nome do pais da cidade
    :return: Retorna o texto do cidade com o pais
    """
    print(f'A cidade {nomeCity} esta localizado em {pais}')


describe_city('Rio de Janeiro')
describe_city('Maceio')
describe_city('New york')
