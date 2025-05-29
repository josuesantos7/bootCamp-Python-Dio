# método In

print("Método In")
contatos = {
    "guilherme@gmail.com": {
        "nome": "Guilherme",
        "telefone": "1234-5678"
    },
    "alexandra@gmail.com": {
        "nome": "Alexandra",
        "telefone": "8765-4321"
    },
}

print("Guilherme está no dicionário de contatos?")
resultado = "guilherme@gmail.com" in contatos
print(resultado)
print()

print("João está no dicionário de contatos?")
resultado = "joao@gmail.com" in contatos
print(resultado)
print()