# Métodos de classes listas:

# [].append() - Adiciona um elemento ao final da lista.
print(".append():")
lista = [1, 2, 3]
lista.append(4)
print(lista)
print("Adicionado o elemento 4 ao final da lista.")
print()


# [].insert() - Adiciona um elemento em uma posição específica da lista.
print(".insert():")
lista = [1, 2, 3]
lista.insert(1, 1.5)
print(lista)
print("Adicionado o elemento 1.5 na posição 1 da lista.")
print()


# [].remove() - Remove o primeiro elemento com o valor especificado.
print(".remove():")
lista = [1, 2, 3, 2, 25]
lista.remove(2)
print(lista)
print("Removido o primeiro elemento com o valor 2 da lista.")
print()


# [].pop() - Remove o último elemento da lista e o retorna.
print(".pop():")
lista = [1, 2, 3]
ultimo_elemento = lista.pop()
print(lista)
print(f"Removido o último elemento da lista: {ultimo_elemento}.")
print("O último elemento da lista foi removido e retornado.")
print()

# [].clear() - Remove todos os elementos da lista.
print(".clear():")
lista = [1, 2, 3]
lista.clear()
print(lista)
print("Todos os elementos da lista foram removidos.")
print()


# [].index() - Retorna o índice do primeiro elemento com o valor especificado.
print(".index():")
lista = [1, 2, 3, 2, 25]
indice = lista.index(2)
print(lista)
print(f"O índice do primeiro elemento com o valor 2 é: {indice}.")
print()


# [].count() - Retorna o número de vezes que um valor aparece na lista.
print(".count():")
lista = [1, 2, 3, 2, 25]
contagem = lista.count(2)
print(lista)
print(f"O valor 2 aparece {contagem} vezes na lista.")
print()


# [].sort() - Ordena os elementos da lista em ordem crescente.
print(".sort():")
lista = [3, 1, 2]
lista.sort()
print(lista)
print("A lista foi ordenada em ordem crescente.")
print()


# [].reverse() - Inverte a ordem dos elementos da lista.
print(".reverse():")
lista = [1, 2, 3]
lista.reverse()
print(lista)
print("A ordem dos elementos da lista foi invertida.")
print()


# [].copy() - Retorna uma cópia superficial da lista.
print(".copy():")
lista = [1, 2, 3]
copia_lista = lista.copy()
print(lista)
print(copia_lista)
print("Uma cópia superficial da lista foi criada.")
print()


# [].extend() - Adiciona os elementos de um iterável ao final da lista.
print(".extend():")
lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)
print("Os elementos [4, 5] foram adicionados ao final da lista.")
print()


# [].join() - Junta os elementos de uma lista em uma string, usando um separador especificado.
print(".join():")
lista = ["a", "b", "c"]
separador = ", "
string_unida = separador.join(lista)
print(string_unida)
print("Os elementos da lista foram unidos em uma string usando o separador ', '.")
print()


# [].split() - Divide uma string em uma lista, usando um separador especificado.
print(".split():")
string = "a, b, c"
separador = ", "
lista_dividida = string.split(separador)
print(lista_dividida)
print("A string foi dividida em uma lista usando o separador ', '.")
print()