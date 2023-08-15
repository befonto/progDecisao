'''
Crie um programa que pergunte a idade do usuário
e em seguida informe se este usuário é menor de idade ou maior de idade.
'''

idade = int(input("Insira a sua idade: "))

# lógica do op ternário2:
# var = resultado verdadeiro if teste condicional else resultado falso

resposta = "Você é maior de idade" if idade >= 18 else "Você é menor de idade"

print(resposta)