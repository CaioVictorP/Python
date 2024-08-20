num = int("Digite o primeiro número: ")
num2 = int("Digite o segundo número")
oper = input("Digite a operação")
if oper == "+":
    result = num + num2
    print(f"A soma de {num} e de {num2} é de {result}")
elif oper == "-":
    result = num - num2
    print(f"A subtração de {num} e de {num2} é de {result}")
elif oper == "*":
    result = num * num2
    print(f"A multiplicação de {num} e de {num2} é de {result}")
elif oper == "/":
    result = num / num2
    print(f"A divisão de {num} e de {num2} é de {result}")
else:
    print("Operação inválida!")