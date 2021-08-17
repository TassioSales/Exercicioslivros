class Carro():
    """Uma tentativa simples de representar uma carro"""
    def __init__(self, make, model, year): #Inicializa os atributos que descrevem  um carro;
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0  
        
    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante"""
        long_name = ("{} {} {}".format(str(self.year), self.make, self.model)) 
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This cas has {} miles on it".format(str(self.odemeter_reading)))
        
    def update_odemeter(self, milage ):
        """Define o valor de leitura do hodometro com valor especificado"""
        if milage >= self.odemeter_reading:
            self.odemeter_reading = milage
        else:
            print('Você não pode reverter um hodômetro!')
            
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odemeter_reading += miles
        
if __name__ == "__main__":
    
    carro1 = Carro('audi', 'a4', 2016)
    carro2 = Carro("Ford", "Palio", 2020)
    
    print(Carro.get_descriptive_name(carro1))
    carro1.update_odemeter(23500)
    carro1.increment_odometer(100)
    print(Carro.read_odometer(carro1))
    print(Carro.get_descriptive_name(carro2))
    carro2.update_odemeter(31)
    print(Carro.read_odometer(carro2))