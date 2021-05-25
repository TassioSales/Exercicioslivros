"""Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum.
"""


def make_album(nomeArtista, nomeAlbum, numFaixas = ''):
    """

    :param nomeArtista: Recebe o nome de uma artista
    :param nomeAlbum: Recebe o nome de uma album
    :param numFaixas: Recebe o numero de faixas do album
    :return: Retorna o album completo em dicionario:
    """
    if numFaixas.isnumeric():
        album = {"Nome": nomeArtista, 'Album': nomeAlbum, 'Numero de Faixas': numFaixas}
    else:
        album = {"Nome": nomeArtista, 'Album': nomeAlbum}
    print(album)


make_album('Leonardo', 'loucuras')
make_album('Anita', 'So de putaria')
make_album('Shakira', 'Forever', '15')
make_album('Marcelo D2', 'Malandragem', '12')