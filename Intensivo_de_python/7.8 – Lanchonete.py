""": Crie uma lista chamada sandwich_orders e a preencha com
os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu
sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
prontos, mostre uma mensagem que liste cada sanduíche preparado"""
sandwich_orders = ['bomba', 'suruba', 'passafome', 'orgulhoso', 'infarto', 'sopradoido', 'mexicano']
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


