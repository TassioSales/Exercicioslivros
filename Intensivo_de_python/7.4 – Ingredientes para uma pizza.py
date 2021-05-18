pizza = []
cont = 0
while True:
    ingrediente = str(input('Digite os ingrediente da sua pizza: ')).lower()
    print(f'Irei adicionar o {cont + 1}ª ingrediente {ingrediente} na sua pizza')
    print('Digite Exit caso não queira mais adicionar mais ingrediente')
    pizza.append(ingrediente)
    cont += 1
    if ingrediente == 'exit':
        print('Muito obrigado sua pizza esta sendo levada para o forno:')
    elif cont > 10:
        cont = cont - 1
        print('Muito obrigado, Porem voce ja atingiu o limite maximo de ingredientes das sua pizza, digite Exit para encerrar o programa, que loga estaremos levando sua pizza para o forno')


print('Estou feliz que tenha escolhido seus ingredientes')
print(f'O ingredientes da sua pizza foram {pizza}')
print('Obrigado pela preferencia')    