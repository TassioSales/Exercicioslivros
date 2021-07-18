"""# Acrescente um  atributo chamado login_attempts à sua classe  User  do  Exercício  9.3  (página  226).  Escreva  um  método  chamado increment_login_attempts()  que  incremente  o  valor  de  login_attempts  em  1. Escreva  outro  método  chamado  reset_login_attempts()  que  reinicie  o  valor  de login_attempts com 0.Crie  uma  instância  da  classe  User  e  chame  increment_login_attempts() várias  vezes.  Exiba  o  valor  de  login_attempts  para  garantir  que  ele  foiincrementado  de  forma  apropriada  e,  em  seguida,  chamereset_login_attempts().  Exiba  login_attempts  novamente  para  garantir  queseu valor foi reiniciado com 0."""

class User(object):
    def __init__(self,nome,sobrenome, cpf, raca, idade):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.cpf = cpf 
        self.raca = raca 
        self.idade = idade
        self.logar = 0
        
    def describe_user(self):
        print(f"{self.nome} {self.sobrenome}")
        print(f"CPF:{self.cpf}")
        print(f"raca:{self.raca}")
        print(f"Idade:{self.idade}")
        print("\n")
    
    def greet_user(self):
        print(f"Seja bem vindo {self.nome} {self.sobrenome}")
        print(f"Quantidade de login ate o momento foi = {self.logar}")
        
    def increment_login_attempts(self):
        self.logar += 1
        
    def reset_login_attempts(self):
        self.logar = 0
        print(f"Quantidade de login do usuario {self.nome} foi resetada para  = {self.logar}")
        
        
if __name__ == "__main__":
    user1 = User("Tassio", "Sales", "11122233345", "Pardo", 31)
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.reset_login_attempts()
    user1.greet_user()
    user1.describe_user()
    
    
    
    
    user2 = User("Cassio", "Sales", "000000000", "Pardo", 28)
    user2.increment_login_attempts()
    user2.increment_login_attempts()
    user2.increment_login_attempts()
    user2.increment_login_attempts()
    user2.greet_user()
    user2.describe_user()
    
    user3 = User("Jhon", "Presley", "22233344456", "Amarelo", 27)
    user3.increment_login_attempts()
    user3.increment_login_attempts()
    user3.increment_login_attempts()
    user3.increment_login_attempts()
    user3.greet_user()
    user3.describe_user()
    
    
    
    user1.reset_login_attempts()
    user2.reset_login_attempts()
    user3.reset_login_attempts()    
    
    