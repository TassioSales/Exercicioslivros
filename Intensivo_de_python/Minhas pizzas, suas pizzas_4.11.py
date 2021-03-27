"""4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
um laço for para exibir a segunda lista. Certifique-se de que cada pizza
nova esteja armazenada na lista apropriada"""

pizzas = ['calabres', 'portuguesa', 'frango com catupiry']

friend_pizzas = pizzas[:]

pizzas.insert(0, "Moda da casa")
friend_pizzas.append("banana")
print("Minha pizza favoritas são:", end=" ")
for pizza in pizzas:
    print(pizza, end=", ")
print("\n", end="")
print("As pizzas favoritas do meu amigo são:", end=" ")
for pizza in friend_pizzas:
    print(pizza, end=", ")