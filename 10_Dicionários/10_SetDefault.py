# Método SetDefault

print("Método SetDefault")
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

x = contatos.setdefault("guilherme@gmail.com", "Giovanna")
print(x)
print(contatos)

print("OBS: se a chave já existir(guilherme@gmail.com), o valor não será alterado para 'Giovanna'.")