import requests

def consultar_cep(cep):
    # Remove espaços ou traços que o usuário possa digitar
    cep = cep.replace("-", "").replace(" ", "")
    
    # Validação básica de tamanho
    if len(cep) != 8 or not cep.isdigit():
        print("[ERRO] Formato de CEP inválido. Digite apenas 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status() # Verifica erros de conexão (ex: 404 ou 500)
        
        dados = resposta.json()
        
        # A API ViaCEP retorna "erro": true se o CEP não existir na base deles
        if "erro" in dados:
            print(f"[FALHA] O CEP {cep} não foi encontrado na base de dados.")
        else:
            print("\n--- INFORMAÇÕES DO ENDEREÇO ---")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro:     {dados.get('bairro', 'N/A')}")
            print(f"Cidade:     {dados.get('localidade', 'N/A')}")
            print(f"Estado:     {dados.get('uf', 'N/A')}")
            print("-" * 30)

    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha na requisição: Verifique sua conexão com a internet.")

# --- Execução ---
print("--- Consulta de CEP ---")
entrada = input("Digite o CEP (apenas números): ")
consultar_cep(entrada)