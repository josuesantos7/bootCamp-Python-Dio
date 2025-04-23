# Operadores Lógicos

# Operador E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite # falso


# Operador OU
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite # True


# Operador Negação
contatos_emergencia = []

not 1000 > 1500 # true

not contatos_emergencia # True

not "saque 1500;" # false

not "" # true

# ------------------------------------------------------
# Exercício:
print("--------------------------------------------------")
print("Exercício")

Saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_2 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_2)