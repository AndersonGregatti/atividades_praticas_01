from datetime import datetime

def calcular_dias_vividos():
    try:
        # 1. Solicita a data de nascimento
        data_input = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        
        # 2. Converte a string para um objeto de data real
        data_nascimento = datetime.strptime(data_input, "%d/%m/%Y")
        
        # 3. Pega a data e hora exata de agora
        data_atual = datetime.now()
        
        # 4. Subtrai as datas (o Python já calcula os bissextos aqui)
        diferenca = data_atual - data_nascimento
        
        # 5. Extrai apenas os dias do resultado
        dias = diferenca.days
        
        if dias < 0:
            print("A data de nascimento não pode ser no futuro!")
        else:
            print(f"Você está vivo há {dias:,} dias!".replace(',', '.'))
            
    except ValueError:
        print("Formato inválido! Por favor, use o formato DD/MM/AAAA.")

# Chama a função
calcular_dias_vividos()