n = int(input("Quantos contribuintes serão cadastrados? "))
for i in range(1, n + 1):
    nome = input((f"Digite o nome do {i}º contribuinte:\n"))
    cpf = input(f"Digite o CPF do {i}º paciente:\n")
    renda = float(input(f"Digite a renda do {i}º contribuinte:\n"))
    print(f"A renda do contribuinte {nome}, CPF de número {cpf}: {renda:.2f}")
    if renda < 1903.99:
        print("Alíquota de dedução do imposto: Isento")
    elif renda < 2826.66:
        print("Alíquota de dedução do imposto: 7.5%")
    elif renda < 3751.06:
        print("Alíquota de dedução do imposto: 15%")
    elif renda < 4664.28:
        print("Alíquota de dedução do imposto: 22.5%")
    else:
        print("Alíquota de dedução do imposto: 27.5%")
