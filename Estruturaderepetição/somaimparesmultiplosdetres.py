soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:  # Verifica se é múltiplo de 3
        print(c)
        soma = soma + c
print("A soma de todos os valores ímpares múltiplos de 3 é:", soma)
