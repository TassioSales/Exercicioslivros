"""Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez."""


def sanduiche(*ingrediente):
    print(f'Os ingredientes são {ingrediente}')


sanduiche('alface', 'tomate', 'peperone')
sanduiche('salsicha', 'batata', 'picles')
sanduiche('salmao', 'choyo', 'maionese')
