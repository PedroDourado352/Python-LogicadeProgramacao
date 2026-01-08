nome = input("Digite seu nome completo: ")

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
total_letras = len(nome.replace(" ", "")) 
primeiro_nome = nome.split()[0]


print("Seu nome maiusculo é:", nome_maiusculo)
print("Seu nome minusculo é:", nome_minusculo)
print("Total de letras no seu nome:", total_letras)
print("Total de letras no seu primeiro nome:", len(primeiro_nome))
print('seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome, len(primeiro_nome)))
