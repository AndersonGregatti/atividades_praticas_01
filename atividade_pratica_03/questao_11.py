# Conversor de Temperatura

print("--- Conversor de Temperatura ---")
temp = float(input("Digite o valor da temperatura: "))
origem = input("unidade de origem (C, F, K) ").upper()
destino = input("Unidade de destino (C, F, K)").upper()

if origem == destino:
    resultado = temp

# De Celsius para...
elif origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    elif destino == "K":
        resultado = temp + 273.15

# De Fahrenheit para...
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    elif destino == "K":
        resultado = (temp - 32) * 5/9 + 273.15


# Conversor de Temperatura

print("--- Conversor de Temperaturas ---")
temp = float(input("Digite o valor da temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

# Lógica de Conversão
if origem == destino:
    resultado = temp
    
# De Celsius para...
elif origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    elif destino == "K":
        resultado = temp + 273.15

# De Fahrenheit para...
elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) * 5/9
    elif destino == "K":
        resultado = (temp - 32) * 5/9 + 273.15

# De Kelvin para...
elif origem == "K":
    if destino == "C":
        resultado = temp - 273.15
    elif destino == "F":
        resultado = (temp - 273.15) * 9/5 + 32

else:
    resultado = None
    print("Unidade inválida!")

if resultado is not None:
    print(f"\nResultado: {temp}{origem} equivale a {resultado:.2f}{destino}")