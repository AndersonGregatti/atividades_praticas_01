# Dados da viagem
distancia_percorrida = float(input("Digite a distancia percorrida em Km: "))
combustivel_gasto = float(input("digite o combustivel gasto em litros: "))

# Cálculo do consumo médio

consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos resultados
print("--- Relatório de Consumo ---")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo Médio: {consumo_medio:.2f} km/l")