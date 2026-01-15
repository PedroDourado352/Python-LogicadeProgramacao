'''for c in range(1, 10,):
    print("Contagem:", c)
print("fim")'''

c = 1
while c < 10:
    print(c)
    c = c + 1
print("fim")

n = 1
while n != 0:
    n = int(input("Digite um número: "))
print("Fim")

r = "S"
while r == "S":
    n = int(input("Digite um número: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("Fim")