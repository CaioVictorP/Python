while True:
    nome = input("Digite o seu nome: ")
    while True:
        peso = float(input("Digite o seu peso(Kg): "))
        altura = float(input("Digite a sua altura(m): "))
        imc = peso / altura ** 2
        if imc <= 0:
            print("IMC inválido!")
        else:
            break
    if imc < 18.5:
        print(f"{nome} tem um IMC de {imc:.1f} que é abaixo do peso normal")
    elif imc >= 18.5 and imc < 25:
        print(f"{nome} tem um IMC de {imc:.1f} que está na média de peso")
    elif imc >= 25 and imc < 30:
        print(f"{nome} tem um IMC de {imc:.1f} que é um excesso de peso")
    elif imc >= 30 and imc < 35:
        print(f"{nome} tem um IMC de {imc:.1f} que é uma obesidade classe I")
    elif imc >= 35 and imc < 40:
        print(f"{nome} tem um IMC de {imc:.1f} que é uma obesidade classe II")
    else:
        print(f"{nome} tem um IMC de {imc:.1f} que é uma obesidade classe III")
    final = input("Digite 1 para terminar ")
    if final == "1":
        print("Terminando...")
        break
    else:
        print("Continuando")