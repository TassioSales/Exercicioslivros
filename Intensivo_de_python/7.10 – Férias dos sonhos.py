"""Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
código que apresente os resultados da enquete."""

LugarDosSonho = []
while True:
    LugarDosSonho.append(input('Se pudesse visitar um lugar do mundo, para onde você iria?'))
    opt = str(input('Deseja continuar ? [S/N]')).split()[0].lower()
    if opt == 's':
        continue
    elif opt == 'n':
        break
    else:
        print('Opção digitada incorreta')
        continue
print('Locais que voce deseja visita ')
for lugar in LugarDosSonho:
    print(f'Voce deseja ir para {lugar}')
