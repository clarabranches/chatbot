from datetime import datetime
import random

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
agora = datetime.now()
ano = str(agora.year)
mes = str(agora.month)
dia = str(agora.day)
hora = str(agora.hour)
minuto = str(agora.minute)
segundo = str(agora.second)
final = ""

def gerar_protocolo():
    global final
    for n in range(4):
        gerado = random.choices(numeros)
        final += str(gerado[0])
    protocolo = (ano+mes+dia+hora+minuto+segundo+final)

if(agora.hour>=6 and agora.hour<12):
    boasvindas = "Bom dia"
elif(agora.hour>=12 and agora.hour<18):
    boasvindas = "Boa tarde"
else:
    boasvindas = "Boa noite"

def atendimento():
    clienteounao = int(input(f"Olá, {boasvindas}. \nMe chamo Ambosio e sou o assistente virtual da (nome_empresa).😄 \nPara dar inicio ao seu atendimento, por favor, digite o número referênte a uma das opções abaixo: \n1 - Já sou Cliente \n2 - Ainda não sou Cliente\n"))
    if(clienteounao == 1):
        print("Fico feliz em rever você")
    elif(clienteounao == 2):
        print("O que posso fazer para que possa se juntar a nós?")
    else:
        print("Opção invalida!")
        atendimento()

atendimento()