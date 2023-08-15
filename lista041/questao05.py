'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor da média obtida pelo aluno.
'''

not1 = float(input("Insira a primeira nota: "))
not2 = float(input("Insira a segunda nota: "))
not3 = float(input("Insira a terceira nota: "))
not4 = float(input("Insira a quarta nota: "))

con = (not1 + not2 + not3 + not4) / 4

if ( con >= 5 ):
    print(f"Sua média foi {con}. Felizmente, você está aprovado!")

else:
    print(f"Sua média foi {con}. Infelizmente, você está reprovado!")