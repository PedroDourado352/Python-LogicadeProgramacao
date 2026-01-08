tabuada = int(input("Digite um número para ver a tabuada: "))

print("Tabuada do", tabuada, ":")
for i in range(1, 11):  
    resultado = tabuada * i
    print(tabuada, "x", i, "=", resultado)