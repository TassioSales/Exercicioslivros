"""Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente.
"""


def make_shirt(tamanhoDaCamisa="G", fraseDaEstampa='Eu amo Python'):
    """
    :param tamanhoDaCamisa: Recebebe o tamanho da camisa
    :param fraseDaEstampa: Recebe o a frase da camisa
    :return: retorna o valor da camisa
    """
    print(f'O tamanho da camisa e {tamanhoDaCamisa}')
    print(f'A frase que sera colocada e {fraseDaEstampa}')


make_shirt()
make_shirt('M')
