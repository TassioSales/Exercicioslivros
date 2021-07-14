# Usando a lista sandwich_orders do Exercício 7.8, garanta
# que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
# Acrescente um código próximo ao início de seu programa para exibir uma
# mensagem informando que a lanchonete está sem pastrami e, então, use um
# laço while para remover todas as ocorrências de 'pastrami' e
# sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
# finished_sandwiches.

sandwich_orders = ['saturno','pastrami','pastrami','jupiter','pastrami','neturno', 'marte','pastrami']

finished_sandwiches = []

print("estamos sem sanduiche da pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sanduiche in sandwich_orders:
    print(f"Preparei seu sanduiche {sanduiche}")
    finished_sandwiches.append(sanduiche)
print(f'lista final de pedidos foi {finished_sandwiches}')
    