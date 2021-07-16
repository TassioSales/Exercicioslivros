"""Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente"""

def make_shirt(mensagem, tamanho= "G"):
    print(f"O tamanho da camiseta e {tamanho}")
    print(f"A messagem que devera ser estampada e {mensagem}")
    
make_shirt("So sei que nada sei", "M")
make_shirt(tamanho = "G", mensagem = "E coisa de maluco")
make_shirt("maluco blz", "P")
make_shirt(mensagem = "sei nao em")