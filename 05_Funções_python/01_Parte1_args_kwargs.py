# Args e Kwargs
# args usa * e Kwargs usa **

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro: {marca} / {modelo} / {placa} / {ano}')

salvar_carro(** {"marca":"Fusca", "modelo":"Fusca", "ano":1970, "placa":"ABC-1234"})

print(" Outro Exemplo:")

def exibir_poema(data_extenso, *args, **kwargs):
    text = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{text}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terça-feira, 05 de Maio de 2025","Zen Of Python", "Beautifull is better than ugly.", autor="Tim Peters", ano=1999)