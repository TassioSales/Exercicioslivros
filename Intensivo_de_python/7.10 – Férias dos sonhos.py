# Escreva um programa que faça uma enquete sobre as
# férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
# pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
# código que apresente os resultados da enquete.


lugares_do_sonho = []

while True:
    
    lugar = str(input('Se pudesse visitar um lugar do mundo, para onde você iria ? '))
    lugares_do_sonho.append(lugar)
    
    opt =  str(input('Deseja continuar [S/N] ?')).upper().split()[0]
    if opt == 'S':
        continue
    else:
        break
print("Os lugares que teve como resultado foram ")

for local in lugares_do_sonho:
    print(local)