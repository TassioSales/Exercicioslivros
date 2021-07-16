"""Comece  com  o  trabalho  feito  no  Exercício  8.10.Chame  a  função  make_great()  com  uma  cópia  da  lista  de  nomes  de  mágicos.Como a lista original não será alterada, devolva a  nova lista e armazene-a em umalista  separada.  Chame  show_magicians()  com  cada  lista  para  mostrar  que  vocêtem  uma  lista  de  nomes  originais  e  uma  lista  com  a  expressão  o  Grandeadicionada ao nome de cada mágico."""

nomesDeMagicos = ["Dafo", "Scire", "Ameth","Dayonis","Thelema","Artemis","Tanith","Robert","Olwen and Loic",'Robat',"Verbius","Silver RavenWolf","Apollo Alenquer "]

Chameshow_magicians = []


def ler_lista_magicos(magicos):
    for magico in magicos:
        print(magico)

def muda_lista_magico(magicos,oGradeMagico):
    for magico in magicos:
          magico = f"O Grande {magico}"
          oGradeMagico.append(magico)


muda_lista_magico(nomesDeMagicos[:],Chameshow_magicians)
ler_lista_magicos(nomesDeMagicos)
ler_lista_magicos(Chameshow_magicians)