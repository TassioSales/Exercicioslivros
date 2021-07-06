#  Modifique o seu programa do Exercício 6.2 (página
# 147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
# apresente o nome de cada pessoa, juntamente com seus números favoritos.


num_favorito = {"Tassio":{17,15,21,40}, "Julia":{28,30,78,44}, "Lucas":{20,56,23,21}, "Cassio":{28,88,99,100,65}}

for favorito in num_favorito:
    print(f"O {favorito} tem com numeros favoritos {num_favorito[favorito]}")