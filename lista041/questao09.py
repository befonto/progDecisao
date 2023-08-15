'''
9)	Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou nulo.
'''

num =  int(input("Insira um número: "))

if ( num > 0 ):
    print(f"{num} é um número positivo!")

elif (num < 0 ):
    print(f"{num} é um número negativo!")

else:
    print(f"{num} é um número nulo!")