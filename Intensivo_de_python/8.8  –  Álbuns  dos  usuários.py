# Comece  com  o  seu  programa  do  Exercício  8.7.Escreva um  laço  while  que  permita  aos  usuários  fornecer  o  nome  de  um  artista  e  otítulo  de  um  álbum.  Depois  que  tiver  essas  informações,  chame  make_album()  comas  entradas  do  usuário  e  apresente  o  dicionário  criado.  Lembre-se  de  incluir  um valor de saída no laço while.

def make_album(album, cantor, faixa = 0):
    albums = {'album': album, "cantor":cantor, "faixa": faixa}
    return albums


while True:
    I_album = str(input("Qual o nome do album: "))
    I_cantor = str(input("Digite o nome do cantor: "))
    I_faixa = int(input("Digite o numero de faixas: "))
    play_list = make_album(I_album, I_cantor, I_faixa)
    print(play_list)
    
    opt = str(input("Deseja continuar [S/N]: ")).lower().split()[0]
    
    if opt == "s":
        pass
    else:
        break