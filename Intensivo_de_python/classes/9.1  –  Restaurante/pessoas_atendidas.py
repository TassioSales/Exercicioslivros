""" Comece  com  seu  programa  do  Exercício  9.1  (página225).  Acrescente  um  atributo  chamado  number_served  cujo  valor  default  é  0.  Crie uma  instância  chamada  restaurant  a  partir  dessa  classe.  Apresente  o  número  de clientes  atendidos  pelo  restaurante  e,  em  seguida,  mude  esse  valor  e  exiba-o novamente.Adicione  um  método  chamado  set_number_served()  que  permita  definir  o número de clientes atendidos. Chame esse método com um novo número e mostre o valor novamente.Acrescente  um  método  chamado  increment_number_served()  que  permita incrementar  o  número  de  clientes  servidos.  Chame  esse  método  com  qualquer número  que  você  quiser  e  que  represente  quantos  clientes  foram  atendidos,  por exemplo, em um dia de funcionamento"""

class Restaurante(object):
    def __init__(self, restaurant_name,cuisine_type, ativo):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.ativo = ativo
        self.number_served = 9
        
    def describe_restaurant(self):
        print(f"Nosso restaurante {self.restaurant_name.title()} e especializado em comida {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        self.ativo = True
        print("Restaurante esta aberto")
        
    def close_restaurant(self):
        self.ativo = False
        print("Restaurante fechado")
    
    def set_number_served(self):
        print("O numero de clientes do restaurante " + self.restaurant_name + " e " + str(self.number_served))
    
    def increment_number_served(self, clientes):
        self.number_served += clientes
        
        
if __name__ == "__main__":
    restaurant1 = Restaurante('Terra nuestra','Italiana', False)
    restaurant1.increment_number_served(4)
    restaurant1.describe_restaurant()
    restaurant1.set_number_served()
    restaurant2 = Restaurante("Burgao da esquina", "Sanduiches", True)
    restaurant2.increment_number_served(6)
    restaurant2.describe_restaurant()
    restaurant2.set_number_served()
    restaurant3 = Restaurante("Japa", "Japonesa", True)
    restaurant3.increment_number_served(7)
    restaurant3.describe_restaurant()
    restaurant3.set_number_served()
