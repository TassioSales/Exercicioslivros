"""Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
166mensagem informando que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de 'pastrami' e
sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
finished_sandwiches."""

sandwich_orders = ['bomba', 'suruba', 'pastrami', 'passafome', 'orgulhoso','infarto', 'pastrami', 'sopradoido',
                   'mexicano', 'pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
cont = 0
while cont < len(sandwich_orders):
    print(f'O sanduiche {sandwich_orders[cont]} esta pronto')
    finished_sandwiches.append(sandwich_orders[cont])
    sandwich_orders.remove(f'{sandwich_orders[cont]}')
    cont += 1
print('\n')
print('Os Sanduiches pedidos foram:')
for sanduiche in finished_sandwiches:
    print(sanduiche, end=',')
print(sandwich_orders)
