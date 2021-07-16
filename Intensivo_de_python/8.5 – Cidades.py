# Escreva uma função chamada describe_city() que aceite o
# nome de uma cidade e seu país. A função deve exibir uma frase simples, como
# Reykjavik está localizada na Islândia. Forneça um valor default ao
# parâmetro que representa o país. Chame sua função para três cidades
# diferentes em que pelo menos uma delas não esteja no país default

def describe_city(cidade, pais = "Brasil"):
    print(f"{cidade} está localizada na {pais}")


describe_city("Toquio", "Japão")
describe_city("Paris", "França")
describe_city("Brasilia")