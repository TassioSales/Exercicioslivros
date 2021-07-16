# Comece com  uma  cópia  de  seu  programa  do  Exercício 8.9.  Escreva  uma  função  chamada  make_great()  que  modifique  a  lista  de mágicos  acrescentando  a  expressão  o  Grande  ao  nome  de  cada  mágico.  Chameshow_magicians() para ver se a lista foi realmente modificada.

nomesDeMagicos = ["Dafo", "Scire", "Ameth","Dayonis","Thelema","Artemis","Tanith","Robert","Olwen and Loic",'Robat',"Verbius","Silver RavenWolf","Apollo Alenquer "]

Chameshow_magicians = []


def ler_lista_magicos(magicos):
    for magico in magicos:
        print(magico)

def muda_lista_magico(magicos,oGradeMagico):
    for magico in magicos:
          magico = f"O Grande {magico}"
          oGradeMagico.append(magico)


muda_lista_magico(nomesDeMagicos,Chameshow_magicians)
ler_lista_magicos(Chameshow_magicians)