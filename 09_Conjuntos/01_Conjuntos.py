# Conjuntos:

# Set
print("Set:")
set([1, 2, 3, 1, 3, 4])
print(set([1, 2, 3, 1, 3, 4]))
print("OBS: Remove os item duplicados e não mantém a ordem.")
print()

set("abacaxi")
print(set("abacaxi"))
print("OBS: Converte uma string em um conjunto de caracteres únicos.")
print()


print("Quando for usar o set e querer usar o valor, é preciso transformar em uma lista!")
print("Exemplo:")
numeros = set([1, 2, 3, 2])
numeros = list(numeros)
print(numeros[0])
print(numeros)
print()


# Iterar conjuntos
print("Iterar conjuntos:")
carros = {"Fusca", "Civic", "Palio", "Gol"}
for carro in carros:
    print(carro)

# Função Enumerate
print("Função Enumerate:")
carros = {"Fusca", "Civic", "Palio", "Gol"}
for i, carro in enumerate(carros):
    print(f"{i}, {carro}")

