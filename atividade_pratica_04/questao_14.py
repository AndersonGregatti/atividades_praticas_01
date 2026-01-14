notas = []

while True:
    try:
        entrada = input("Digite uma nota de (0 a 10) ou 'fim' para sair: ")
        
        if entrada.lower() == 'fim':
            break
            
        nota = float(entrada) 
        
        if nota < 0 or nota > 10:
            raise Exception() # Lança a exceção se a nota for fora do limite

        notas.append(nota) # Adiciona a nota apenas se ela for válida

    except ValueError:
        print("Erro: Você deve digitar apenas números.")
    except Exception:
        print("Erro: Nota inválida! Digite um valor entre 0 e 10.")

# --- Cálculo fora do loop (após digitar 'fim') ---
if len(notas) > 0:
    soma = 0
    for n in notas:
        soma += n  # Soma cada nota da lista

    media = soma / len(notas)
    print(f"\n--- Resultado Final ---")
    print(f"Notas digitadas: {notas}")
    print(f"Média final: {media:.2f}")
else:
    print("Nenhuma nota foi registrada.")
