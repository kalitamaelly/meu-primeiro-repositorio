alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.5},
    {"nome": "Daniel", "nota": 5.5},
    {"nome": "Eduarda", "nota": 7.0}
]

# Ordenar da maior para a menor nota
ordenados = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)

print("Alunos ordenados:")
print(ordenados)

# Filtrar alunos com nota maior ou igual a 7
aprovados = filter(lambda aluno: aluno["nota"] >= 7, alunos)

print("\nAlunos aprovados:")
for aluno in aprovados:
    print(aluno["nome"])

