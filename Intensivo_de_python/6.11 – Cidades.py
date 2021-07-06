# Crie um dicionário chamado cities. Use os nomes de três
# cidades como chaves em seu dicionário. Crie um dicionário com informações
# sobre cada cidade e inclua o país em que a cidade está localizada, a
# população aproximada e um fato sobre essa cidade. As chaves do dicionário
# de cada cidade devem ser algo como country, population e fact. Apresente o
# nome de cada cidade e todas as informações que você armazenou sobre ela.

cities = {"Brasilia": {"População estimada": 3.055149, 'Pais': 'Brasil', 'fact': 1.934210},
          "Rio de Janeiro": {'População estimada': 17.366189, 'Pais': "Brasil", 'fact': 7.087797},
          "São Paulo": {"População estimada": 46.289333, "Pais": "Brasil", 'fact': 30.778960}
          }
for cidade in cities:
    print('{} tem uma população de {} fica localizado no {} e possui mais de {} veiculos'.format(cidade, cities[cidade][
        "População estimada"], cities[cidade]["Pais"], cities[cidade]["fact"]))
