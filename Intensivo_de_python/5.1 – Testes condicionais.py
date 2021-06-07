""" Escreva uma série de testes condicionais. Exiba uma
frase que descreva o teste e o resultado previsto para cada um. Seu código
deverá ser semelhante a: car = 'subaru'
print("Is car == 'subaru'? I predict True.") print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.") print(car == 'audi') •
Observe atentamente seus resultados e certifique-se de que compreende
por que cada linha é avaliada como True ou False.
• Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como
True e outros cinco avaliados como False."""

nome = 'Tassio Sales'

print(nome == 'Sales Tassio')
print(nome ==  'Tassio Sales')
print(nome.upper() == 'tassio sales')
print(nome.upper() == 'TASSIO SALES')
print(nome.lower() == 'tassio sales')
print(nome.lower() == 'TASSIO SALES')
print(nome.capitalize() == 'Tassio Sales')
print(nome.title() == 'Tassio sales')
print(nome.isnumeric())
print(nome.isalnum())
print(nome.isalpha())
print(nome.isprintable())