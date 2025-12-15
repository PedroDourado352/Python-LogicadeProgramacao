larg = float(input("Digite a largura da parede em metros: "))
alt = float(input("Digite a altura da parede em metros: "))
area = larg * alt

print(f"A área da parede é de {area:.2f} metros quadrados.")

tinta = area / 2
print(f"Para pintar a parede, você precisará de {tinta:.2f} litros de tinta.")