while True:
    try:
        # 1. Adicionado ':' após o try e corrigida a indentação
        senha = input("\nDigite a senha (ou 'sair' para encerrar): ")

        if senha.lower() == "sair":
            print("Saindo do programa...")
            break

        # 2. Validação de tamanho
        if len(senha) < 8:
            raise Exception("A senha tem que ter ao menos 8 caracteres.")
        
        # 3. Validação de números
        tem_numero = False
        for caractere in senha:
            if caractere in '0123456789':
                tem_numero = True
                break
        
        # O teste do 'tem_numero' deve ser FORA do for acima
        if not tem_numero:
            raise Exception("A senha deve conter ao menos um número.")
        
        # Se chegar aqui, a senha é válida
        print("Senha Válida cadastrada com sucesso!")
        break

    except Exception as e:
        # Exibe a mensagem de erro definida no 'raise'
        print(f"Erro: {e}")