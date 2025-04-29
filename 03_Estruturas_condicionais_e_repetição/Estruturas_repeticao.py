# Estruturas de repetição:

# FOR:
texto = input('Digite um texto: ')
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

print()
print("-" * 20)


# FOR/ELSE:
texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print("Não há vogais no texto!")
print()

print("Função Range:")
# RANGE:
list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()


# Utilizando range com FOR:
for numero in range(10):
    print(numero, end=" ")


# Exibindo a tabuada do 5:
for numero in range(0, 51, 5):
    print(numero, end=" ")


print("Função While:")
# WHILE:
opcao = -1

while opcao != 0:
    opcao = int(input("Digite [1] para sacar \n[2] Extrato \n[0] sair: "))
    print("Você digitou:", opcao)

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Extrato bancário")


print("While/Else:")
# While/Else:
while opcao != 0:
    opcao = int(input("Digite [1] para sacar \n[2] Extrato \n[0] sair: "))
    print("Você digitou:", opcao)

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Extrato bancário")
else:
    print("Obrigado por utilizar nosso sistema!")


# Usando o Break:
while True:
    opcao = int(input("Digite um número: "))
    print("Você digitou:", opcao)

    if numero == 10:
        print("Você digitou dez!")
        break
    print("Fim da execução!")