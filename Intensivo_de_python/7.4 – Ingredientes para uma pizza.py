# Escreva um laço que peça ao usuário para
# fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
# fornecido. À medida que cada ingrediente é especificado, apresente uma
# mensagem informando que você acrescentará esse ingrediente à pizza.

while True:
    print("digite quit para sair do programa")
    pergunta = str(input("Qual ingrediente deseja adicionar a pizza ? ")).lower()
    
    if pergunta == "quit":
        print("Seus ingredientes foram adicionaddos a sua pizza")
        break
    else:
        print(f"O ingrdiente {pergunta} foi adicionado a pizza")