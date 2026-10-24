alunos = [
    {"nome": "Alice", "nota": 8},
    {"nome": "João", "nota": 5},
    {"nome": "Carla", "nota": 9},
    {"nome": "Daniel", "nota": 6}
   ]
aprovados = 0
for aluno in alunos:
    if aluno["nota"] >= 7:
        print(aluno["nome"])
        aprovados += 1

print("Total de alunos aprovados:", aprovados)
