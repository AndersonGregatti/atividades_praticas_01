while True:
    try:
        # Entrada dos números
        numero1 = float(input("\nDigite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        # print("Operações: + | - | * | /")
        operacao = input("Digite a operação desejada: ")

        
        # Processamento do cálculo
        if operacao == '+':
            resultado = numero1 + numero2
        elif operacao == '-':
            resultado = numero1 - numero2
        elif operacao == '*':
            resultado = numero1 * numero2
        elif operacao == '/':
            if numero2 == 0:
                print("Erro: Não é possível dividir por zero!")
                continue
            resultado = numero1 / numero2
        else:
            print("Operação inválida! Tente novamente.")
            continue

        print(f"Resultado: {numero1} {operacao} {numero2} = {resultado:.2f}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")