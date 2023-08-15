'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Insira um número inteiro: "))
num2 = int(input("Insira outro número inteiro: "))

a = num2 % num1

if ( a == 0 ):
    print(f"O número {num1} é divisível por {num2}!")

else:
    print(f"O número {num2} não é divisível por {num1}!")
