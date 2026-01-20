import csv

def escrever_csv(nome_arquivo, dados):
    try:
        # Correções: 'with' em vez de 'whit', 'newline' com 'l' minúsculo
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            
            # Escreve o cabeçalho
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            
            # Escreve as linhas de dados
            for linha in dados:
                escritor.writerow(linha)
                
        return f"Dados escritos com sucesso no arquivo '{nome_arquivo}'"
    except Exception as e:
        return f"Erro ao escrever o arquivo: {e}"

# Correção: 'São Paulo' precisa estar entre aspas (string)
dados = [
    ['Joao', 25, 'São Paulo'],
    ['Maria', 30, 'Rio de Janeiro'],
    ['Pedro', 22, 'Belo Horizonte']
]

nome_arquivo = input('Digite o nome do arquivo csv (ex: dados.csv): ')
print(escrever_csv(nome_arquivo, dados))