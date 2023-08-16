'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso) correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o número inserido não corresponder à um dia da semana.
'''

num17 = int(input("Insira um número de 1 a 7 de acordo com o dia da semana que deseja saber: "))

if ( num17 == 1 ):
    print("Domingo!")

elif ( num17 == 2 ):
    print("Segunda-feira!")

elif ( num17 == 3 ):
    print("Terça-feira!")

elif ( num17 == 4 ):
    print("Quarta-feira!")

elif ( num17 == 5 ):
    print("Quinta-feira!")

elif (num17 == 6 ):
    print("Sexta-feira!")

elif (num17 == 7 ):
    print("Sábado!")

else:
    print("Número inválido. Tente novamente! ")