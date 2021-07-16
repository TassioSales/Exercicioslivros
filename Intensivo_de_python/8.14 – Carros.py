#  Escreva  uma  função  que  armazene  informações  sobre  um  carro  em um  dicionário.  A  função  sempre  deve  receber  o  nome  de  um  fabricante  e  um modelo.  Um  número  arbitrário  de  argumentos  nomeados  então  deverá  ser  aceito.Chame  a  função  com  as  informações  necessárias  e  dois  outros  pares  nome-valor,por  exemplo,  uma  cor  ou  um  opcional.  Sua  função  deve  ser  apropriada  para  umachamada como esta


def carros_info(fabricante, modelo, **carros_informacoes):
    carro = {}
    carro['fabricante'] = fabricante
    carro['modelo'] = modelo
    for key, value in carros_informacoes.items():
        carro[key] = value
    return carro

carro_1 = carros_info("ford", "fiesta", ano = 1990, cor = "Rosa", dividas = False)

print(carro_1)
