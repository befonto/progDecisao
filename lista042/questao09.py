'''
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de idade, se é maior de idade, ou se é maior de 65 anos.
'''

idade = int(input("Insira a sua idade: "))

if ( idade < 18 ):
    print(f"Você é menor de idade!")

elif ( idade >= 18 and idade < 65 ):
    print(f"Você é maior de idade!")

else:
    print(f"Você possui mais de 65 anos de idade!")
