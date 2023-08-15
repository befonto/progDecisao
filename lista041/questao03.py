'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou é ímpar.
'''

num = int(input("Insira um número: "))
ta = num%2

if ( ta == 1 ):
    print(f"{num} é um número ímpar!")

elif ( ta == 0 ):
    print(f"{num} é um número par!")