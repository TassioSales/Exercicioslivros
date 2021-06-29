"""Crie uma lista com cinco ou mais nomes de usuários, incluindo
o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá
uma saudação a cada usuário depois que eles fizerem login em um site.
Percorra a lista com um laço e mostre uma saudação para cada usuário: 
• Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá
admin, gostaria de ver um relatório de status?
• Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por
fazer login novamente."""

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
        print(f'Seja Bem vindo, Sistema pronto pára uso {user}')