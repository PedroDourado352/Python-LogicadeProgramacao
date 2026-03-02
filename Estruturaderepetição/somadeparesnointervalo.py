A = int(input("Digite o valor de A: ")  )
B = int(input("Digite o valor de B: ")  )  ####Inserção de dados

inicio = min(A, B)   #Pega o menor número entre A e B
fim = max(A, B)      #Pega o maior número entre A e B

soma = 0 #criar variavek chamada soma e atribuir o valor 0 a ela

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += i

print(f"A soma dos números pares entre {inicio} e {fim} é: {soma}")
