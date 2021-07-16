"""Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido"""

def city_country(cidade, pais):
    return f"{cidade}, {pais}"

p1 = city_country("Brasilia", "Brasil")
p2 = city_country("Paris", "França")
p3 = city_country("Roma", "Italia")


print(f"{p1}\n {p2}\n {p3}")    