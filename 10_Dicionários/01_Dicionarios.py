# Dicionários

print("Dicionários")
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(pessoa)
print()

print("add um novo elemento")
pessoa["telefone"] = "1234-5678"
print(pessoa)

print("---" * 20)

print("Acessando valores")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

print("---" * 20)

print("Diciário aninhado")
pessoa_aninhada = {
    "nome": "Maria",
    "idade": 25,
    "endereco": {
        "rua": "Rua A",
        "numero": 123,
        "cidade": "Rio de Janeiro"
    }
}

print("O uso do anhinhamento de dicionários permite armazenar informações complexas.")
print("Nome:", pessoa_aninhada["nome"])
print("Endereço:", pessoa_aninhada["endereco"]["rua"], pessoa_aninhada["endereco"]["numero"], pessoa_aninhada["endereco"]["cidade"])
print()

print("---" * 20)
print()

print("Iterando sobre um dicionário")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")