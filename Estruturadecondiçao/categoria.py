categoria = input("Digite a categoria: ")
preco = 0

if categoria == "1":
    preco = 100
elif categoria == "2":
    preco = 200
elif categoria == "3":
    preco = 300

print(f"O preço da categoria {categoria} é: {preco}")