def mostralinha():
    print("-" * 30)

mostralinha()

def mensagem(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)

mensagem("Sistema de Teste")

def titulo(txt):
    print("-" * 30)
    print(txt)
    print("-" * 30)

titulo("Curso de Python no YouTube")

def contador(*num):
    print(num )
    
contador(2, 1, 7)
contador(8, 0)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

valores = [7, 2, 5, 0, 4]
dobra(valores)


