num1 = int(input("Digite o primeiro número: ")) # Comandos de entradas de numeros
num2 = int(input("Digite o segundo número: "))

operation = input("Digite a operação (+, -, *, /): ") # Escolher operação 

if operation == "+":
    result = num1 + num2
    print(f"O resultado da adição é: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"O resultado da subtração é: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"O resultado da multiplicação é: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"O resultado da divisão é: {result}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")