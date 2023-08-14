'''
Crie um programa que pergunte dois núemros ao usuário.
Em seguida o programa deverá somar os dois números e
apresentar o resultado se o valor for maior que 10.
'''

num1 =  int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

soma = num1 + num2

if ( soma > 10 ):
    print(f"A soma dos valores inseridos é {soma}")
    print("FIM DO PROGRAMA")

else:
    print("A soma dos valores é menor que 10!")


