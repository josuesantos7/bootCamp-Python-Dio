# Indentação e Blocos:
# Python utiliza 4 espaços para definir blocos de código.

# exemplo:
# def sacar(self, valor:float) -> None:
#     if self.saldo >= valor:
#        self.saldo -= valor
#        print(self.saldo)
        

def sacar(valor:float):
    saldo = 1000

    if saldo >= valor:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

sacar(250)