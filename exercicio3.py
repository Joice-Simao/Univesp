"""
Exercício 2. Cap. 4 – Ex 3c
 Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis 
 N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado 
 com média” se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno Reprovado com 
 média”. Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
"""

N1 = float(input("Digite a nota 1: "))
N2 = float(input("Digite a nota 2: "))
N3 = float(input("Digite a nota 3: "))
N4 = float(input("Digite a nota 4: "))

MD = float(N1 + N2 + N3 + N4 / 4)

if(MD >= 5):
    print(f"Aluno Aprovado com média {MD:.1f}")

else:
     print(f"Aluno Reprovado com média {MD:.1f}")