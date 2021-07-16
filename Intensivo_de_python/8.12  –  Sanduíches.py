# Escreva  uma  função  que  aceite  uma  lista  de  itens  que  uma pessoa  quer  em  um  sanduíche.  A  função  deve  ter  um  parâmetro  que  agrupe  tantos itens  quantos  forem  fornecidos  pela  chamada  da  função  e  deve  apresentar  um resumo  do  sanduíche  pedido.  Chame  a  função  três  vezes  usando  um  númerodiferente de argumentos a cada vez

lista_ingrediente = ["queijo", "alface", 'tomate', 'cebola', "picles", "hamburgue","pao", "bacon"]


def montar_sanduiche(*ingredientes):
    for itens in ingredientes:
        print(itens)

montar_sanduiche(lista_ingrediente)