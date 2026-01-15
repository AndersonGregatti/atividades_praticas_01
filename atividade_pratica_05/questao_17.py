def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem.
    """
    # Cálculo: valor total multiplicado pela porcentagem dividida por 100
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de Interação com o Usuário
try:
    conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10, 15): "))

    valor_da_gorjeta = calcular_gorjeta(conta, porcentagem)
    total_com_gorjeta = conta + valor_da_gorjeta

    print(f"\n--- Detalhes do Pagamento ---")
    print(f"Conta: R$ {conta:.2f}")
    print(f"Gorjeta ({porcentagem}%): R$ {valor_da_gorjeta:.2f}")
    print(f"Total a pagar: R$ {total_com_gorjeta:.2f}")

except ValueError:
    print("Erro: Insira valores numéricos válidos.")