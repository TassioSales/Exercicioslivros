"""Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço parnia exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
"""

rios = {"Amazonas":{"NOME":"Amazonas", "LOCALIZACAO":"Brasil","TAMANHO":6.992},
        "Nilo":{"NOME":"Nilo", "LOCALIZACAO":"Egito", "TAMANHO":6.852},
        "Yangtze":{"NOME":"Yangtze", "LOCALIZACAO":"China", "TAMANHO":6.380}}


for rio in rios.values():
    print('O rio {} fica localizado em maior parte no {} seu tamanho total e {:.3f} Km'.format(rio['NOME'], rio['LOCALIZACAO'], rio ['TAMANHO']))
    
   

