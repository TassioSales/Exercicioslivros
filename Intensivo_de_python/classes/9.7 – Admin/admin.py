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
        self.privilegios = ["can add post", "candelete post", "can ban user"]
    
    def show_privileges(self):
        print(f"O usuario {self.nome} tem")
        for item in self.privilegios:
            print(f"Privilegio de adm {item}")
    
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
    
    user4 = Admin('Cassia', "Luciana", "111122225", "Branca", 18)
    user4.greet_user()
    user4.describe_user()
    user4.show_privileges()