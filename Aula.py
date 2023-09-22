while True:
    nome = input("Digite o seu nome: ")
    estciv = input("""Digite o seu estado civil: 
                   S -> Solteiro/a

                   C -> Casado/a

                   V -> Viuvo/a

                   D -> Desquitado/a
                   """)
    estciv = estciv.upper()
    if estciv not in ("S", "C", "V", "D", "SOLTEIRO", "CASADO", "DIVORCIADO", "DESQUITADO"):
        print("Digite apenas S/C/V/D!")
    else:
        if estciv in ("S", "SOLTEIRO"):
            estciv = "Solteiro/a"
        elif estciv in ("C", "CASADO"):
            estciv = "Casado/a"
        elif estciv in ("V", "VIUVO"):
            estciv = "Viuvo/a"
        else:
            estciv = "Desquitado/a"
        print(f"{nome} é {estciv}")
        final = input("Digite 1 para repetir ")
        if final == "1":
            print("Recomeçando...")
        else:
            print("Terminando")
            break