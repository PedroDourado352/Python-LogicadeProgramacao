dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilômetros foram percorridos? "))
pago = (dias * 60) + (km * 0.15)
print(f"O total a pagar pelo aluguel do carro é de R$ {pago:.2f}.") 