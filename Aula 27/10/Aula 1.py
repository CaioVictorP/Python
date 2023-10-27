while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    metodo = input("Digite a operação: (+, -, *, /) ")
    if metodo == "+":
        resultado = num1 + num2
        print(f"O resultado da soma é {resultado}")
    elif metodo == "-":
        resultado = num1 - num2
        print(f"O resultado da subtração é {resultado}")
    elif metodo == "*":
        resultado = num1 * num2
        print (f"O resultado da multiplicação é {resultado}")
    elif metodo == "/":
        resultado = num1 / num2
        print(f"O resultado da divisão é {resultado}")
    else:
        print("Operação inválida! Coloque apenas +, -, * ou /!")
    end = input("Deseja continuar? (S/N): ")
    end = end.upper()
    print(end)
    if end == "N":
        break