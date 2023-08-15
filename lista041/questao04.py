'''
4)	Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por 4 e 5”.
'''

vn =  int(input("Insira um número inteiro: "))

a = vn % 4

b = vn % 5

if ( a == 0 and b == 0):
    print(f"{vn} é divisível por 4 e 5!")

else:
    print(f"{vn} não é divisível por 4 e 5!")
