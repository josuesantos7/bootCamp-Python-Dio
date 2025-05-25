# Iterando Listas:

# Percorrendo a lista com o For
carros = ["gol", "celta", "uno", "palio", "civic"]

for carro in carros:
    print(carro)

# Função Enumarate
for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")
    