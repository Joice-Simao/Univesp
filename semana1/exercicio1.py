#Exercício 1. Cap. 3 – Ex 4a
#Ler uma temperatura em graus Celsius e apresentá-la convertida
#em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
#sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

temperatura = int(input("Digite a temperatura em Celsius - "))

fahrenheit = int(temperatura * 9 / 5 + 32)

print(temperatura,"°C =", fahrenheit,"°F")