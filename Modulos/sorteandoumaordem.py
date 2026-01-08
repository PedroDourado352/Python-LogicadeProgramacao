import random

primeiro_aluno = str(input("Digite o nome do primeiro aluno: "))
segundo_aluno = str(input("Digite o nome do segundo aluno: "))
terceiro_aluno = str(input("Digite o nome do terceiro aluno: "))
quarto_aluno = str(input("Digite o nome do quarto aluno: "))

lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(lista_alunos)
print("A ordem de apresentação será:")