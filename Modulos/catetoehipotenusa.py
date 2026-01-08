import math

cateto_oposto = float(input("Digite o valor do cateto oposto: ").replace(',', '.'))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: ").replace(',', '.'))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print("O valor da hipotenusa é {:.2f}".format(hipotenusa))