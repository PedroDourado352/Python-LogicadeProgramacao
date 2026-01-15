def terreno(largura, comprimento):
    largura = float(input("Largura (m): "))
    comprimento = float(input("Comprimento (m): "))
    area = largura * comprimento
    print(f"A área do terreno de {largura}m x {comprimento}m é de {area}m².")

terreno(0, 0)