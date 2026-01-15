def eh_palindromo(texto):
    texto_limpo = ''
    for letra in texto:
        if letra.isalnum():
            texto_limpo += letra.lower()

    invertido = ''
    for letra in texto_limpo:
        invertido = letra + invertido  # Constrói a string de trás para frente

    # CORREÇÃO: O nome da variável deve ser 'invertido'
    if texto_limpo == invertido:
        return "Sim"
    else:
        return "Não"
    
texto = input("Digite um texto: ")
resultado = eh_palindromo(texto)
print(f"'{texto}' é um palíndromo? {resultado}")