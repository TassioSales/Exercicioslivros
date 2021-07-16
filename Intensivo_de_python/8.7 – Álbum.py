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

def make_album(album, cantor, faixa = 0):
    albums = {'album': album, "cantor":cantor, "faixa": faixa}
    return albums
    
    
    
album1 =  make_album('A vida', "Roberto carlos", 15)
album2 =  make_album('Solitude', "Raugil", 8)
album3 =  make_album('Coisa chata', "Romario")

print(album1)
print(album2)
print(album3)