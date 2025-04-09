"""
Exercício 2.2 Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
- A soma de 2 e 2 é menor que 4.
- O valor de 7 // 3 é igual a 1 + 1.
- A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
- A soma de 2, 4 e 6 é maior que 12.
- 1387 é divisível por 19.
- 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
- O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
"""

comando1 = 2 + 2 < 4

if comando1 == True:
    print("Verdadeiro")

else:
    print("Falso")

comando2 = 7 // 3 == (1 + 1)

if comando2 == True:
    print("Verdadeiro")
else:
    print("Falso")

comando3 = (3 ** 2) + (4 ** 2) == 25

if comando3 == True:
    print("Verdadeiro")
else:
    print("Falso")

comando4 = 2 + 4 + 6 > 12

if comando4 == True:
    print("Verdadeiro")
else:
    print("Falso")

comando5 = 1387 % 19 == 0

if comando5 == True:
    print("Verdadeiro")
else:
    print("Falso")

comando6 = 31 % 2 == 0

if comando6 == True:
    print("Verdadeiro")
else:
    print("Falso")

comando7 = 34.99 or 29.95 or 31.50 < 30.00

if comando7 == True:
    print("Verdadeiro")
else:
    print("Falso")   