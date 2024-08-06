while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    metodo = input("Digite a operação: (+, -, *, /) ")
    if metodo == "+" or metodo == "-" or metodo == "*" or metodo == "/":
        resultado = eval(num1 + metodo + num2)
        print(f"{resultado:.2f}")
    else:
        print("Operação inválida! Coloque apenas +, -, * ou /!")
    end = input("Deseja continuar? (S/N): ")
    end = end.upper()
    print(end)
    if end == "N":
        break