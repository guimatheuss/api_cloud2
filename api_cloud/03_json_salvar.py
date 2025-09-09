import json

# Lista de alunos (simulando dados que poderiam vir da nuvem)
alunos = [
    {"nome": "João", "curso": "ADS"},
    {"nome": "Maria", "curso": "CC"},
    {"nome": "Ana", "curso": "ADS"}
]

# Salvando em arquivo local
with open("alunos.json", "w") as f:
    json.dump(alunos, f, indent=4)

print("Arquivo 'alunos.json' salvo com sucesso!")
print()