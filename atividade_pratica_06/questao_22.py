import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        # Realiza a requisição à API
        resposta = requests.get(url, timeout=10)
        
        # Verifica se a conexão foi bem-sucedida (Status Code 200)
        resposta.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        usuario = dados['results'][0]
        
        # Extraindo as informações solicitadas
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibindo os resultados
        print("-" * 30)
        print("USUÁRIO ENCONTRADO")
        print("-" * 30)
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        print("-" * 30)

    except requests.exceptions.RequestException as erro:
        # Captura qualquer erro de conexão (timeout, DNS, 404, 500, etc)
        print(f"\n[ERRO] Falha na conexão com a API.")
        print(f"Detalhes: {erro}")

if __name__ == "__main__":
    buscar_usuario()