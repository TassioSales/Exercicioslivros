"""Uma  sorveteria  é  um  tipo  específico  de  restaurante.  Escreva  uma classe  chamada  IceCreamStand  que  herde  da  classe  Restaurant  escrita  no Exercício 9.1 (página 225)  ou no Exercício  9.4 (página 232). Qualquer  versão da classe  funcionará;  basta  escolher  aquela  de  que  você  mais  gosta.  Adicione  uma tributo  chamado  flavors  que  armazene  uma  lista  de  sabores  de  sorvete.  Escrevaum  método  para  mostrar  esses  sabores.  Crie  uma  instância  de  IceCreamStand  e chame esse método."""

class Restaurante():
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
        
class Sorveteria(Restaurante):
    
    def __init__(self, restaurant_name,cuisine_type, ativo, flavors):
        super().__init__(restaurant_name, cuisine_type, ativo)
        self.flovors = flavors
        
        
if __name__ == "__main__":
    restaurant1 = Restaurante('Terra nuestra','Italiana', False)
    restaurant1.describe_restaurant()
    restaurant2 = Restaurante("Burgao da esquina", "Sanduiches", True)
    restaurant2.describe_restaurant()
    restaurant3 = Restaurante("Japa", "Japonesa", True)
    restaurant3.describe_restaurant()
    