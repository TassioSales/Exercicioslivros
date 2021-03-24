"""Se pudesse convidar alguém, vivo ou morto, para o
jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
que você gostaria de convidar para jantar. Em seguida, utilize sua lista para
exibir uma mensagem para cada pessoa, convidando-a para jantar.
"""

listaJantar = ['Mara', 'Ana', 'Joana', 'Flavia', 'Marcela', 'Julia']

print(f'Bem vinda {listaJantar[0]}')
print(f'Welcome {listaJantar[1]}')
print(f'Velkommen {listaJantar[2]}')
print(f'Welina {listaJantar[3]}')
print(f'Croeso {listaJantar[4]}')
print(f'Kaabo {listaJantar[5]}')

print("\n")

"""3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
    • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
    no final de seu programa, especificando o nome do convidado que não
    poderá comparecer.
    • Modifique sua lista, substituindo o nome do convidado que não poderá
    comparecer pelo nome da nova pessoa que você está convidando.
    • Exiba um segundo conjunto de mensagens com o convite, uma para cada
    pessoa que continua presente em sua lista."""
print(f'''Nao poderam vir para o jantar
{listaJantar[0]}, {listaJantar[1]}, {listaJantar[2]}, {listaJantar[3]}, {listaJantar[4]}, 
e a convidade {listaJantar[5]} confirmou presença''')

listaJantar[0] = "Kananda"
listaJantar[1] = "Fernanda"
listaJantar[2] = "Kalica"
listaJantar[3] = "Brenda"
listaJantar[4] = "Thais"
print("\n")

print("No lugar das pessoas que nao poderam vir"
      "foram convidadas essas pessoas. ")
print(f'Bem vinda {listaJantar[0]}')
print(f'Welcome {listaJantar[1]}')
print(f'Velkommen {listaJantar[2]}')
print(f'Welina {listaJantar[3]}')
print(f'Croeso {listaJantar[4]}')

print("\n")

"""3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista.
"""
listaJantar.insert(0, "Maria")
listaJantar.insert(3, 'Marcela')
listaJantar.append("Mara")

print(f'Hello {listaJantar[0]}')
print(f'talofa {listaJantar[1]}')
print(f'Hallå {listaJantar[2]}')
print(f'Ahoj {listaJantar[3]}')
print(f'Hola {listaJantar[4]}')
print(f'Bonjour {listaJantar[5]}')
print(f'Kamusta {listaJantar[6]}')
print(f'zdravo {listaJantar[7]}')
print(f'Hallo {listaJantar[8]}')

print("\n")
print(listaJantar),
print("\n")


"""3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas
pessoas para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até
que apenas dois nomes permaneçam em sua lista. Sempre que remover um
nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
saiba que você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam
na lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
uma lista vazia no final de seu programa."""

print("Infelizmente so poderei chamar 2 pessoas\n")

print(f'sinte muito por não poder convidá-la {listaJantar[0]}')
print(f'Sinto muito por não poder convidá-la {listaJantar[1]}')
print(f'Sinto muito por não poder convidá-la {listaJantar[2]}')
print(f'Sinto muito por não poder convidá-la {listaJantar[3]}')
print(f'Sinto muito por não poder convidá-la {listaJantar[4]}')
print(f'Sinto muito por não poder convidá-la {listaJantar[5]}')
print(f'Sinto muito por não poder convidá-la {listaJantar[6]}')

listaJantar.pop(0)
listaJantar.pop(1)
listaJantar.pop(2)
listaJantar.pop(3)
listaJantar.pop(4)
listaJantar.pop(0)
listaJantar.pop(1)

print("\n")

print(listaJantar)

del listaJantar[0]
del listaJantar[0]
print("\n")
print(listaJantar)

