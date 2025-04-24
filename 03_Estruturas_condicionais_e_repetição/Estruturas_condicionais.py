# Estruturas condicionais:

print("Exemplo de if")
# etapa 1: If / if-else / elif
# if:
saldo = 2000
saque = float(input("Digite o valor do saque: "))
if saldo >= saque:
    print("Saque realizado com sucesso!")

if saldo < saque:
    print("Saldo insuficiente!")

# if-elif-else:
print("Exemplo de if-elif-else")
import sys

opcao = int(input("Digite a opção desejada: [1] Sacar \n[2] Extrato"))

if opcao == 1:
    valor = float(input("Digite o valor do saque: "))

elif opcao == 2:
    print("Exibindo extrato...")
else:
    sys.exit("Opção inválida!")

print("- " * 20)

print(" Segundo exemplo de if-elif-else")

MAIORIDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Digite sua idade: "))

if idade >= MAIORIDADE:
    print("Maior de idade, pode tirar a CNH!")
elif idade >= IDADE_ESPECIAL:
    print("pode fazer a auta teórica, mas não pode fazer a prova prática!")
else:
    print("Menor de idade, não pode tirar a CNH!")


print("- " * 20)
print("Exemplo de if-elif-else aninhado")
# etapa 2: If aninhado:
saldo = 1000
cheque_especial = 400
conta_normal = True
conta_universitaria = False

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial!")
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o gerente!")


print("- " * 20)
print("Exemplo de if ternário")
# etapa 3: If ternário
saldo = 300
saque = 60

status = "Sucesso" if saldo >= saque else "Falha!"

print(f"Resultado do saque: {status}")