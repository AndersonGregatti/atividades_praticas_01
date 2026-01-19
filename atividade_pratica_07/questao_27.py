import csv

def ler_arquivo(nome_arquivo): # Adicionado ":"
    try:
        # Correções: open(, newline minúsculo, e indentação do except
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
                
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Execução
nome_arquivo = input("Digite o nome do arquivo csv: ")
ler_arquivo(nome_arquivo)