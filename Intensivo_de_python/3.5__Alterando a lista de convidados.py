""" Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não
poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.

"""

nomes_pessoas = ["Ana", "Maria", 'Jose']

print(f'Gostaria de te convidar para um jantar {nomes_pessoas[0]}')
print(f'Gostaria de te convidar para um jantar {nomes_pessoas[1]}')
print(f'Gostaria de te convidar para um jantar {nomes_pessoas[2]}')

print(f'Os convidados {nomes_pessoas[0]}, {nomes_pessoas[1]}, {nomes_pessoas[2]} não iram comparacer\n')


print('IREI CONVIDAR')
nomes_pessoas[0] = "Matheus"
nomes_pessoas[1] = "Lucas"
nomes_pessoas[2] = "Rodrigo"

print(f'Gostaria de te convidar para um jantar {nomes_pessoas[0]}')
print(f'Gostaria de te convidar para um jantar {nomes_pessoas[1]}')
print(f'Gostaria de te convidar para um jantar {nomes_pessoas[2]}')