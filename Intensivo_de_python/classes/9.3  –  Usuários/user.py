"""Crie  uma  classe  chamada  User.  Crie  dois  atributos  de  nomes first_name  e  last_name  e,  então,  crie  vários  outros  atributos  normalmente armazenados  em  um  perfil  de  usuário.  Escreva  um  método  de  nome describe_user()  que  apresente  um  resumo  das  informações  do  usuário.  Escreva outro método chamado greet_user() que  mostre uma  saudação  personalizada ao usuário. Crie  várias  instâncias  que  representem  diferentes  usuários  e  chame  os  dois métodos para cada usuário."""

class User(object):
    def __init__(self,nome,sobrenome, cpf, raca, idade):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.cpf = cpf 
        self.raca = raca 
        self.idade = idade 
        
    def describe_user(self):
        print(f"{self.nome} {self.sobrenome}")
        print(f"CPF:{self.cpf}")
        print(f"raca:{self.raca}")
        print(f"Idade:{self.idade}")
        print("\n")
    
    def greet_user(self):
        print(f"Seja bem vindo {self.nome} {self.sobrenome}")
        
if __name__ == "__main__":
    user1 = User("Tassio", "Sales", "11122233345", "Pardo", 31)
    user1.greet_user()
    user1.describe_user()
    
    
    user2 = User("Cassio", "Sales", "000000000", "Pardo", 28)
    user2.greet_user()
    user2.describe_user()
    
    user3 = User("Jhon", "Presley", "22233344456", "Amarelo", 27)
    user3.greet_user()
    user3.describe_user()