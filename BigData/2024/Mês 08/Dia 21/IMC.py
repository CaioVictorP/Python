n = int(input("Quantos pacientes serão cadastrados? "))
for i in range(1, n + 1):
    nome = input((f"Digite o nome do {i}º paciente:\n"))
    idade = int(input(f"Digite a idade do {i}º paciente:\n"))
    peso = float(input("Digite o peso do {i}º paciente em kg:\n"))
    altura = float(input("Digite a altura do {i}º paciente em metros:\n"))
    imc = peso / (altura ** 2)
    print(f"O IMC do paciente {nome}: {imc:.2f}")
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 24.9:
        print("Classificação: Peso normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    elif imc < 34.9:
        print("Classificação: Obesidade grau 1")
    elif imc < 39.9:
        print("Classificação: Obesidade grau 2")
    else:
        print("Classificação: Obesidade grau 3")
