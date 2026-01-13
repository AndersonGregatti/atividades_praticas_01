# Classificador de idade 

'''crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias: 
Criança (0-12 anos)
Adolecente (13-17 anos)
Adulto (18-59 anos)
Idoso (60 anos ou mais)
'''

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print(f"Categoria: Criança de (0 ate 12 amns ). Idade atual {idade}")

elif idade >= 13 and idade <= 17:
    print(f"Categoria: Adolescente (13 até 17 anos). Idade atual: {idade}")

elif idade >= 18 and idade <= 59:
    print(f"Categoria: Adulto (18 até 59 anos). Idade atual: {idade}")

elif idade >= 60:
    print(f"Categoria: Idoso (60 anos ou mais). Idade atual: {idade}")

else:
    print("Idade inválida! Por favor, digite um número positivo.")
    


