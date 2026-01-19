import json

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            # Correção: Para JSON usamos json.load()
            dados_json = json.load(arquivo_json)
            return dados_json
    except FileNotFoundError:
        return f"Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

def escrever_arquivo(nome_arquivo, dados):
    try:
        # Correção: 'w' deve ser minúsculo
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            # Correções: json.dump (sem acento), ensure_ascii (com 'i'), False (F maiúsculo)
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        return f"Dados escritos com sucesso no arquivo {nome_arquivo}"
    except Exception as e:
        return f"Erro ao escrever no arquivo: {e}"

# Dados organizados como uma lista de dicionários (melhor para JSON)
dados = [
    {"nome": "Joao", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Pedro", "idade": 22, "cidade": "Belo Horizonte"}
]

nome_arquivo = input('Digite o nome do arquivo json (ex: dados.json): ')

# Execução
print(escrever_arquivo(nome_arquivo, dados))