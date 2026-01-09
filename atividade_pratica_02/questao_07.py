# Notas do aluno
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

# Cálculo da média aritmética
# (Soma de todos os valores / Quantidade de valores)
media = (nota1 + nota2 + nota3) / 3

# Exibição dos resultados
print("--- Boletim Escolar ---")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média Final: {media:.2f}")