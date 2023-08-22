def inicializa():
    preco = int(input("Informe o preco do ticket: "))
    return preco

def mostrar_menu(maquina):
    print(f"""MÁQUINA DE TICKETS: [possuo {maquina.dinheiro}]""")
    print("""[a] Inserir Moedas
[b] Imprimir Ticket
[x] Encerrar Operação""")
    pega_resposta(maquina)

def pega_resposta(maquina):
    resposta = input("        ? ")
    match(resposta):
        case "a":
            inserir_moeda(maquina)
        case "b":
            maquina.imprimir_ticket()
            mostrar_menu(maquina)
        case "x":
            encerrar(maquina)

def inserir_moeda(maquina):
    valor = 0
    while(valor!=-1):
        maquina.inserir_dinheiro(valor)
        valor = int(input("Informe a moeda [-1 para parar]: "))
    mostrar_menu(maquina)

def encerrar(maquina):
    print(f"""Total arrecadado: {maquina.total} centavos""")
