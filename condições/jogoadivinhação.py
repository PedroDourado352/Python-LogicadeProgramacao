from random import randint
computador = randint(0, 10)
jogador = (int(input("Em que número eu pensei entre 0 e 10? ")))
print("Sou seu computador... Acabei de pensar no numero:", computador)

if jogador == computador:
    print("Parabéns! Você me venceu!")
else:
    print("Você perdeu! Tente novamente.")



 