# Funções:

def exibir_mensagem():
    print("Olá, Mundo!")
    print("Aprendendo Python!")

nome = "Eduarda"
def exibir_mensagem_2(nome):
    print(f"Seja Bem Vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome)

# Retornando valores:
def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([20,35]))


def retorna_antecessor_e_sucessor       (numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(retorna_antecessor_e_sucessor(10))