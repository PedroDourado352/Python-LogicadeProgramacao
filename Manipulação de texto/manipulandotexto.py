frase = "Curso em Vídeo Python"
frase[9]
print(frase[9:14:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print(len(frase)) # conta quantos caracteres tem a frase, incluindo espaços
print(frase.count("o")) # conta quantas vezes a letra "o" aparece na frase
print(frase.count("o",0,13)) # conta quantas vezes a letra "o" aparece na frase, entre a posição 0 e 13
print(frase.find("Vídeo")) # mostra a posição onde começa a palavra "Vídeo"
print(frase.find("Android")) # se não encontrar a palavra, retorna -1
print("Curso" in frase) # retorna True se a palavra "Curso" estiver na frase
print(frase.replace("Python", "Android")) # substitui a palavra "Python" por "Android"
print(frase.upper()) # transforma todos os caracteres em maiúsculo
print(frase.lower()) # transforma todos os caracteres em minúsculo
print(frase.capitalize()) # transforma o primeiro caractere em maiúsculo e o resto em minúsculo
print(frase.title()) # transforma o primeiro caractere de cada palavra em maiúsculo
print(frase.split()) # divide a frase em uma lista de palavras
print('-'.join(frase)) # une os caracteres da frase com o caractere especificado entre eles

frase2 = "   Aprenda Python  "
print(frase2.strip()) # remove os espaços em branco do início e do fim da frase
print(frase2.rstrip()) # remove os espaços em branco do fim da frase
print(frase2.lstrip()) # remove os espaços em branco do início da frase

