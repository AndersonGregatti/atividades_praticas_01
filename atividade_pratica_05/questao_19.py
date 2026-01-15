def calcular_desconto():
    # d - Interação com usuário: Pede os valores necessários
    try:
        preco_original = float(input("Digite o preço original do produto: R$ "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 15 para 15%): "))

        # a - Cálculo de desconto: Baseado na porcentagem
        valor_desconto = preco_original * (porcentagem_desconto / 100)

        # b - Preço final: Determina o novo preço após o desconto
        preco_final = preco_original - valor_desconto

        # c - Formatação: Arredonda para 2 casas decimais
        print("\n--- Resumo da Compra ---")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
        print(f"Preço Final: R$ {preco_final:.2f}")
        print("------------------------")
        
    except ValueError:
        print("Erro: Por favor, insira apenas números (use ponto para decimais).")

# Executa o programa
calcular_desconto()