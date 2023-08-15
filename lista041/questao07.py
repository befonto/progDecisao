'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Insira um valor positivo ou negativo: "))

if ( num < 0 ):
    print(f"O módulo de {num} é {num * -1}!")

elif ( num > 0 ):
    print(f"O módulo de {num} é {num}!")

