"""Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e
acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True e um
False para cada um dos casos a seguir: • testes de igualdade e de não
igualdade com strings; • testes usando a função lower(); • testes numéricos que
envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e
menor ou igual a; • testes usando as palavras reservadas and e or; • testes
para verificar se um item está em uma lista; • testes para verificar se um item
não está em uma lista.
"""

palavra = 'dinheiro'.upper()
print(palavra)
print(palavra.lower() == 'dinheiro')
print(palavra == 'DINHEIRO')
print(palavra.lower() == 'DINHEIRO')
print(palavra != 'Dinheiro')
print(palavra != 'DINHEIRO')

num = 13
num_1 = 24
num_2 = 56
num_3 = 65

print(num > num_2)
print(num_3 < num_2)
print(num == num)
print(num_1 < num_2)
print(num < num_1 and num < num_2)
print(num_3 > num_2 or num_3 > num_1)

lista = [1, 2, 3, 4, 5]

if 2 in lista:
    print(f'o numero 2 esta na lista')
if 6 not in lista:
    print('O numero 6 nao esta na lista')
