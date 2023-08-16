'''
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e 5000, entre 5001 e 8000, ou acima de 8000.
'''

num = int(input("Insira um número: "))

if ( num < 1000 ):
    print(f"{num} está abaixo de 1000!")

elif ( num < 5001 ):
    print(f"{num} está entre 1000 e 5000!")

elif ( num <= 8000 ):
    print(f"{num} está entre 5001 e 8000!")

else:
    print(f"{num} está acima de 8000!")

