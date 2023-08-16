'''
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e 5000, ou acima de 5000.
'''

num = int(input("Insira um número: "))

if ( num < 1000 ):
    print(f"{num} é um número que está abaixo de 1000!")

elif ( num <= 5000 ):
    print(f"{num} é um número que está entre 1000 e 5000!")

else:
    print(f"{num} é um número que está acima de 5000!")

