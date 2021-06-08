""" Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista."""

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

print('\n')

print("Encontrei uma mesa maior, irei chamar Tassio, Julia, Jhon")

nomes_pessoas.insert(0, "Tassio")
nomes_pessoas.insert(4, "Julia")
nomes_pessoas.append('Jhon')

print(f'Gostaria de te convidar para um jantar {nomes_pessoas[0]}')
print(f'Gostaria de te convidar para um jantar {nomes_pessoas[4]}')
print(f'Gostaria de te convidar para um jantar {nomes_pessoas[-1]}')