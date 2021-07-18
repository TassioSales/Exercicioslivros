"""Comece  com  a   classe  do  Exercício  9.1.  Crie  trêsinstâncias  diferentes  da  classe  e  chame  describe_restaurant()  para  cada instância."""

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
    restaurant2 = Restaurante("Burgao da esquina", "Sanduiches", True)
    restaurant2.describe_restaurant()
    restaurant3 = Restaurante("Japa", "Japonesa", True)
    restaurant3.describe_restaurant()
    