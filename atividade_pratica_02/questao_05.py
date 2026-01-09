# Conversor de Moeda

'''crie um programa que converte um valor em reais para 
dólares e euros. use os seguintes dados: 

Valor em Reais: R$ 100.00
Taxa do Dólar: R$ 5.20
Taxa do Euro: R$ 6.15
o programa deve calcular e exibir os valores convertidos, arrendondando para duas casas decimais.
'''

# Definindo os valores 
valor_reais = float(input("Digite o valor em reais R$")) 
taxa_dolar = 5.37
taxa_euro = 6.25

# Realizando os cálculos de conversão

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Exibindo os resultados formatados com duas casas decimais
print(f"Valor original: R$ {valor_reais:.2f}")
print(f"Conversão para Dólar: $ {valor_dolar:.2f}")
print(f"Conversão para Euro: € {valor_euro:.2f}")

