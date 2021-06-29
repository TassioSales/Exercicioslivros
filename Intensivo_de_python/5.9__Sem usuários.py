usuarios = ['Tassio Sales',
            'Julia Mendonca',
            'Jhon Presley',
            'Lucas Mendonca',
            'Antonio Sales',
            'Admin']
for user in usuarios:
    if user == "Admin":
        print(f'Olá {user}, gostaria de ver um relatório de status?\n')
    else:
        print(f'Seja Bem vindo, Sistema pronto pára uso {user}\n')
        
usuarios.clear()
print(usuarios)

if usuarios == []:
    print('Precisamos encontrar alguns usuários!')