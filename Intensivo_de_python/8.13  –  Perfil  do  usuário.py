"""Comece  com  uma  cópia  de  user_profile.py,  da  página 210.  Crie  um  perfil  seu  chamando  build_profile(),  usando  seu  primeiro  nome  eo sobrenome, além de três outros pares chave-valor que o descrevam"""

def build_profile(first, last, **user_info):    
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""   
    profile = {}     
    profile['first_name'] = first    
    profile['last_name'] = last   
    for key, value in user_info.items():        
        profile[key] = value    
    return profile 
    
    
user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')
user_profile_tassio = build_profile("Tassio", "Sales", nacionalidade = "Brasileiro", idade = "31", altura = 1.83, peso = 90)

print(user_profile)
print(user_profile_tassio)