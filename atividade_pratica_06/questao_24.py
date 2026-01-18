import requests
from datetime import datetime

def consultar_cotacao(moeda):
    # A API espera o formato 'MOEDA-BRL' (ex: USD-BRL)
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        resposta = requests.get(url, timeout=10)
        
        # Se a moeda não existir, a API retorna erro 404
        if resposta.status_code == 404:
            print(f"[ERRO] A moeda '{moeda}' não existe ou não é suportada.")
            return

        resposta.raise_for_status()
        dados = resposta.json()
        
        # O JSON vem com uma chave dinâmica (ex: 'USDBRL')
        chave = f"{moeda}BRL"
        info = dados[chave]
        
        # Extraindo os dados solicitados
        valor_atual = float(info['bid'])
        maxima = float(info['high'])
        minima = float(info['low'])
        data_hora = info['create_date']
        
        print(f"\n--- COTAÇÃO: {moeda} para Real (BRL) ---")
        print(f"Valor Atual: R$ {valor_atual:.2f}")
        print(f"Máxima:      R$ {maxima:.2f}")
        print(f"Mínima:      R$ {minima:.2f}")
        print(f"Atualizado em: {data_hora}")
        print("-" * 40)

    except requests.exceptions.RequestException:
        print("[ERRO] Falha na conexão com o serviço de cotação.")
    except KeyError:
        print(f"[ERRO] Formato de resposta inesperado para a moeda '{moeda}'.")

# --- Interface ---
print("--- Consulta de Moedas (AwesomeAPI) ---")
codigo_moeda = input("Digite o código da moeda (Ex: USD, EUR, BTC, GBP): ").strip()
consultar_cotacao(codigo_moeda)
