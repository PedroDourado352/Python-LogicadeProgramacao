emprestimo = float(input("Digite o valor do empréstimo: "))
salario = float(input("Digite o valor do salário: "))
meses = int(input("Digite o número de meses para pagar o empréstimo: "))

parcela = emprestimo / meses
limite = salario * 0.3

print(f"Valor da parcela: R$ {parcela:.2f}")

if parcela <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado! A parcela excede 30% do salário.")