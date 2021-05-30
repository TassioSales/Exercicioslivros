"""Trabalhando com um dos programas dos
Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma
mensagem informando o número de pessoas que você está convidando para o
jantar.
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

print('\n')

print("Encontrei uma mesa maior, irei chamar Tassio, Julia, Jhon")

nomes_pessoas.insert(0, "Tassio")
nomes_pessoas.insert(4, "Julia")
nomes_pessoas.append('Jhon')

print(f"Estou convidando um total de {len(nomes_pessoas)} pessoas")