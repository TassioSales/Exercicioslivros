from car import ElectricCar

carro2 = ElectricCar('tesla', 'model s', 2016)
print(carro2.get_descriptive_name())
carro2.battery.describe_battery() 
carro2.battery.get_range() 