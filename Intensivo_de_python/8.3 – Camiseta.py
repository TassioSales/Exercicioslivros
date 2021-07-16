#  Escreva uma função chamada make_shirt() que aceite um
# tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
# A função deve exibir uma frase que mostre o tamanho da camiseta e a
# mensagem estampada.


def make_shirt(tamanho, mensagem):
    print(f"O tamanho da camiseta e {tamanho}")
    print(f"A messagem que devera ser estampada e \n{mensagem}")
    
make_shirt("M", "So sei que nada sei")
make_shirt(tamanho = "G", mensagem = "E coisa de maluco")