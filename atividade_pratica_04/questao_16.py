pares = 0
impares = 0
lista_numeros = []

while True:
    try:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        numero = int(entrada) # Convertemos para inteiro
        lista_numeros.append(numero)

        # Lógica para Par ou Ímpar
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1

    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros ou 'fim'.")

# Resumo final
print("-" * 30)
print(f"Análise encerrada!")
print(f"Total de números digitados: {len(lista_numeros)}")
print(f"Quantidade de Pares: {pares}")
print(f"Quantidade de Ímpares: {impares}")
