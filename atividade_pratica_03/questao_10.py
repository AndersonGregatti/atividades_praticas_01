# Calculadora de IMC

peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))

# Calculo do IMC
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")