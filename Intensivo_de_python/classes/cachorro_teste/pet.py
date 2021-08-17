class Dog():
    """Uma tentativa simples de modelar uma cachorro"""
    def __init__(self, name, age): #Inicializando atributos name e age
        self.name = name
        self.age = age
    
    def senta(self): #simula um cachorro sentando em resposta a um comando
        print(f'{self.name.title()} agora está sentado.')
    
    def rola(self): #Simula um cachorro rolando em resposta a um comando
        print(f"{self.name.title()}. rolou")

if __name__ == '__main__':
    cachorro1 =  Dog("Noky", 6)
    cachorro2 = Dog("lucy", 3)
    print("-" * 30)
    
    print(f"O nome do meu cão é {cachorro1.name.title()}.")
    print('Meu cachorro tem {} anos de idade'.format(str(cachorro1.age))) 
    Dog.rola(cachorro1)
    Dog.senta(cachorro1)
    
    print("-" * 30)
    
    print(f"O nome do meu cão é {cachorro2.name.title()}.")
    print('Meu cachorro tem {} anos de idade'.format(str(cachorro2.age))) 
    Dog.rola(cachorro2)
    Dog.senta(cachorro2)     