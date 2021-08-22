""" Um administrador é um tipo especial de usuário. Escreva uma
classe chamada Admin que herde da classe User escrita no Exercício 9.3
(página 226), ou no Exercício 9.5 (página 232). Adicione um atributo
privileges que armazene uma lista de strings como "can add post", "can
delete post" "can ban user", e assim por diante. Escreva um método chamado
show_privileges() que liste o conjunto de privilégios de um administrador. Crie
uma instância de Admin e chame seu método."""

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
        
class Admin(User):
    def __init__(self, nome,sobrenome, cpf, raca, idade):
        super().__init__(nome, sobrenome, cpf, raca, idade)
        self.privilages = Privileges()
    
class Privileges():
    def __init__(self, privilages=[]):
        self.privilages = privilages
        
    def show_privilages(self):
        print(f'\n privilegios:')
        if self.privilages:
            for privilage in self.privilages:
                print(f'    -> {privilage}')
        else:
            print(f'o usuario nao tem')

    
if __name__ == "__main__":

    user4 = Admin('Cassia', "Luciana", "111122225", "Branca", 18)
    user4.greet_user()
    user4.describe_user()
    user4.privilages.privilages  = ["can add post", "candelete post", "can ban user"]
    user4.privilages.show_privilages()
  