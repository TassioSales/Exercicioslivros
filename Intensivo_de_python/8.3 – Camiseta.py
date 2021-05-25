"""Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.
"""


def make_shirt(tamanhoDaCamisa, fraseDaEstampa):
    """
    :param tamanhoDaCamisa: Recebebe o tamanho da camisa
    :param fraseDaEstampa: Recebe o a frase da camisa
    :return: retorna o valor da camisa
    """
    print(f'O tamanho da camisa e {tamanhoDaCamisa}')
    print(f'A frase que sera colocada e {fraseDaEstampa}')


make_shirt("M", 'Eu estou aqui')
make_shirt(tamanhoDaCamisa="G", fraseDaEstampa="A vida e bela")
