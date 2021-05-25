"""Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.
"""


def city_country(cidade=""):
    """
    :param cidade: recebe o nome de uma cidade
    :return: retorna o nome da cidade
    """
    print(cidade, end=',')


city_country('brasilia'.title())
city_country('maceio'.capitalize())
