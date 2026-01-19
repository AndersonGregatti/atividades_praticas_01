import pandas as pd
import os

# Define a pasta de trabalho
pasta_projeto = r'C:\Users\Anderson\projeto_python_udemy\atividade'
nome_arquivo = 'arquivo_log.xlsx' # Certifique-se que o nome e extensão estão corretos

# Junta a pasta com o nome do arquivo de forma segura
caminho_completo = os.path.join(pasta_projeto, nome_arquivo)

try:
    # Lembre-se de instalar: pip install openpyxl
    df = pd.read_excel(caminho_completo)
    print("Arquivo carregado com sucesso!")
    
    media = df['tempo_execucao'].mean()
    print(f"Média: {media:.2f}")

except FileNotFoundError:
    print(f"Erro: O arquivo {nome_arquivo} não foi encontrado na pasta {pasta_projeto}")
except Exception as e:
    print(f"Erro inesperado: {e}")