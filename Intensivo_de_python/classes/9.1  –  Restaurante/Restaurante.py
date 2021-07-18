"""Crie  uma  classe  chamada  Restaurant.  O  método  __init__()de Restaurant  deve  armazenar  dois  atributos:  restaurant_name  e  cuisine_type.Crie  um  método  chamado  describe_restaurant()  que  mostre  essas  duas informações,  e  um  método  de  nome  open_restaurant()  que  exiba  uma mensagem informando que o restaurante está aberto.Crie  uma  instância  chamada  restaurant  a  partir  de  sua  classe.  Mostre  os  dois atributos individualmente e, em seguida, chame os dois métodos."""


class Restaurante(object):
    def __init__(self, restaurant_name,cuisine_type, ativo):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.ativo = ativo
        
    def describe_restaurant(self):
        print(f"Nosso restaurante {self.restaurant_name.title()} e especializado em comida {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        self.ativo = True
        print("Restaurante esta aberto")
        
    def close_restaurant(self):
        self.ativo = False
        print("Restaurante fechado")



        
if __name__ == "__main__":
    restaurant1 = Restaurante('Terra nuestra','Italiana', False)
    restaurant1.describe_restaurant()
    restaurant1.close_restaurant()