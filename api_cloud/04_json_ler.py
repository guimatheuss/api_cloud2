import json

# Abrindo e lendo o arquivo JSON salvo
with open("alunos.json") as f:
    dados = json.load(f)

# Exibindo lista completa
print("Lista de alunos:", dados)

# Percorrendo e mostrando cada aluno
for aluno in dados:
    print(f"{aluno['nome']} - {aluno['curso']}")

print()