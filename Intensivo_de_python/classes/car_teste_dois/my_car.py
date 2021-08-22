from car import Car

carro = Car('audi', 'a4', 2016)
print(carro.get_descriptive_name())
carro.odometer_reading = 23
carro.read_odometer()