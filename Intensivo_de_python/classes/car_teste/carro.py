class Carro():
    """Uma tentativa simples de representar uma carro"""
    def __init__(self, make, model, year): #Inicializa os atributos que descrevem  um carro;
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0
        self.tanque = 0
        
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
      
            
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odemeter_reading += miles
    
    def read_tanque(self):
        print("O carro esta com  {} litros  de combustivel ".format(str(self.tanque)))
    
    def litros_no_tanque(self, litros_gas):
        if litros_gas >= self.tanque:
            self.tanque = litros_gas
            
    def abaster(self, gas):
        self.tanque += gas
    
            
    
class EleriCar(Carro): #Representa aspectos específicos de veículos elétricos.
    def __init__(self, make, model, year):#Inicializa os atributos da classe-pai.
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):#Exibe uma frase que descreve a capacidade da bateria.
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def read_tanque(self):
        print("This car doesn't need a gas tank!")
        
class Battery():#"Uma tentativa simples de modelar uma bateria para um carro elétrico.
    def __init__(self, battery_size=70): #Inicializa os atributos da bateria.
        self.battery_size = battery_size
        
    def describe_battery(self): #Exibe uma frase que descreve a capacidade a bateria.
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
if __name__ == "__main__":
    
    carro1 = Carro('audi', 'a4', 2016)
    carro2 = Carro("Ford", "Palio", 2020)
    carro_eletrico1 = EleriCar('tesla', 'modelo s', 2016)
    
    print(Carro.get_descriptive_name(carro1))
    carro1.update_odemeter(23500)
    carro1.increment_odometer(100)
    carro1.read_tanque()
    print(Carro.read_odometer(carro1))
    
    print("x" * 40)
    
    print(Carro.get_descriptive_name(carro2))
    carro2.update_odemeter(31)
    print(Carro.read_odometer(carro2))
    
    print("x" * 40)
    
    print(carro_eletrico1.get_descriptive_name())
    carro_eletrico1.describe_battery() 
    
    