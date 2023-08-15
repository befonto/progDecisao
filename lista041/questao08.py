'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num =  int(input("Insira um número inteiro: "))

res = "Seu número está entre 1 e 10!" if num >= 1 and num <= 10 else "Seu número não está entre 1 e 10!"

print(res)

'''
Outra forma de fazer:

if ( num >= 1 and num <= 10 ):
    print(f"{num} está entre 1 e 10!")

else:
    print(f"{num} não está entre 1 e 10!")
'''