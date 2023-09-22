while True:
    nome = input("Digite o seu nome: ")
    estciv = input("Digite o seu estado civil(S/C/V/D): ")
    estciv = estciv.upper()
    if estciv != "S" and estciv != "C" and estciv != "V" and estciv != "D":
        print("Digite apenas S/C/V/D!")
    else:
        if estciv == "S":
            estciv = "Solteiro/a"
        elif estciv == "C":
            estciv = "Casado/a"
        elif estciv == "V":
            estciv = "Viuvo/a"
        else:
            estciv = "Divorciado/a"
        print(f"{nome} é {estciv}")
        final = input("Digite 1 para repetir ")
        if final == "1":
            print("Recomeçando...")
        else:
            print("Terminando")
            break
