primeiro_aluno = str(input("Digite o nome do primeiro aluno: "))
segundo_aluno = str(input("Digite o nome do segundo aluno: "))
terceiro_aluno = str(input("Digite o nome do terceiro aluno: "))
quarto_aluno = str(input("Digite o nome do quarto aluno: "))

import random
lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
aluno_sorteado = random.choice(lista_alunos)
print("O aluno sorteado foi: {}".format(aluno_sorteado))