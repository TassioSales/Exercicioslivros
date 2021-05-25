"""Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
um valor de saída no laço while.
"""


def make_album(nomeArtista, nomeAlbum, numFaixas=''):
    album = {'Nome Cantos': nomeArtista, 'Nome do album': nomeAlbum, "Faixas": numFaixas}
    """
    :param nomeArtista: Recebe o nome de uma artista
    :param nomeAlbum: Recebe o nome de uma album
    :param numFaixas: Recebe o numero de faixas do album
    :return: Retorna o album completo em dicionario:
    """
    return album


while True:
    nome = input('Digite o nome do artista: ')
    nomeDoAlbum = input('Digite o nome do album: ')
    faixas = input('Digite o numero de faixas do album: ')
    opt = input('Quer adicinar mais algum album ? [S/N]').split()[0].lower()
    make_album(nome, nomeDoAlbum, faixas)
    albuns = {'Nome Cantos': nome, 'Nome do album': nomeDoAlbum, "Faixas": faixas}
    if opt == 's':
        continue
    else:
        print('Muito obrigado')
        print('Aqui estão seus albuns')
        break
print(albuns)