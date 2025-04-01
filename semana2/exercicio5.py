"""
Exercício 2.1
Escreva expressões algébricas Python correspondentes aos seguintes comandos:
✔ A soma dos 5 primeiros inteiros positivos.
✔ A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
✔ O número de vezes que 73 cabe em 403.
✔ O resto de quando 403 é dividido por 73.
✔ 2 à 10ª potência.
✔ O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
- O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
"""

soma = 0

for i in range(1,6):
    soma += i

print(f"A soma dos 5 primeiros inteiros positivos é: {soma}\n")

media  = int (23 + 19 + 31) / 3
print(f"A idade média é: {media:.0f}\n")


qtd73 = 403 // 73 
print(f" O número de vezes que 73 cabe em 403 é {qtd73}\n")

resto = 403 % 73 
print(f"Resto é {resto}\n")

resultado_potencia = 2 ** 10
print(f"2 à 10ª potência {resultado_potencia}\n")

valorAbosluto = 57 - 54
print(f"O valor absoluto é {valorAbosluto}\n")

precos = [34.99, 29.95, 31.50]
menor_preco = min(precos)
print(f"Menor preço {menor_preco}\n")