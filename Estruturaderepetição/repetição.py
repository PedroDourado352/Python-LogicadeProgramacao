frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

for c in range(5, 0, -1):
    print("Contagem:", c)
print("Feliz Ano Novo!")


for c in range(0, 10, 2):
    print("Contagem:", c)

n= int(input("digite um numero: "))
for c in range(0, n+1):
    print(c)


i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("FIM")