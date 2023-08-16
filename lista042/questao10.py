'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições devem seguir as regras da tabela abaixo:
Média | Situação
Abaixo de 3,0  | Reprovado
Entre 3,0 e 6,9 | Prova Final
A partir de 7,0 | Aprovado

'''

nome = str(input("Insira seu nome: "))
nota1 = float(input("Insira a nota de sua primeira prova: "))
nota2 = float(input("Insira a nota de sua segunda prova: "))

a = (nota1 + nota2) / 2

if ( a < 3.0 ):
    print(f"Você, {nome}, está reprovado(a)! Sua média: {a}!")

elif ( a >= 3.0 and a <= 6.9 ):
    print(f"Você, {nome}, foi encaminhado(a) para a prova final! Sua média: {a}!")

else:
    if ( a >= 7.0 ):
        print(f"Parabéns! Você, {nome}, está aprovado(a)! Sua média: {a}!")