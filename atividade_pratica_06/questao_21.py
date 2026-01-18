import secrets
import string

def gerar_senha(tamanho):
    # Combinação de letras (A-z), números (0-9) e símbolos (!@#...)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

# --- Interface ---
print("--- Gerador de 3 Senhas Seguras ---")

try:
    comprimento = int(input("Digite o tamanho desejado para as senhas: "))
    
    print(f"\nAqui estão 3 opções de senhas com {comprimento} caracteres:\n")
    
    # Gera 3 senhas usando um loop
    for i in range(1, 4):
        senha = gerar_senha(comprimento)
        print(f"Senha {i}: {senha}")
        
    print("\nGuarde-as em um local seguro!")

except ValueError:
    print("Erro: Digite um número inteiro para o tamanho.")

    