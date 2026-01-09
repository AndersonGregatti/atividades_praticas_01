# Dados de entrada
produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculos
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos detalhes
print(f"--- Detalhes da Compra ---")
print(f"Produto: {produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}% (R$ {valor_desconto:.2f})")
print(f"Preço Final: R$ {preco_final:.2f}")