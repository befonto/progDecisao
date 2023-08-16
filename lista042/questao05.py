'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final, informe na tela se o estado inserido está ou não na região Sudeste
'''

est = str(input("Insira a sigla de um estado brasileiro: "))

if ( est == "RJ" or est == "rj" or  est == "Rj" or est == "SP" or est == "sp" or  est == "Sp" or est == "MG" or  est == "mg" or est == "Mg" or est == "ES" or est == "Es" or est == "es"):
    print(f"{est} é um estado brasileiro que está localizado na região Sudeste.")

else:
    print(f"{est} é um estado brasileiro que não está localizado na região Sudeste.")

