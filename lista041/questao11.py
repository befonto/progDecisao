'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado somente o algarismo das centenas.
'''

num = int(input("Insira um número inteiro de três algarismos: "))

if ( num >= 100 and num <= 999 ):
    cent = num // 100
    print(f"O algarismo das centenas de {num} é {cent}")

else:
    print(f"O valor inserido não possui três algarismos!")

'''
Outra forma
num = int(input("Insira um número inteiro de três algarismos: "))

a = int( num / 100 )

if (num >= 100):
    print(f"O algarismo das centenas é {a}!")
'''