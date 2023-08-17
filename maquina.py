class MaquinaDeVendas:
    def __init__(self,preco,dinheiro,total):
        self.preco = preco
        self.dinheiro = dinheiro
        self.total = total

    def inserir_dinheiro(self,valor):
        self.dinheiro = self.dinheiro + valor

    def imprimir_ticket(self):
        if(self.dinheiro>=self.preco):
            print(f"""####################
       TICKET
    {self.preco} centavos
####################""")

        else:
            print("O dinheiro inserido na máquina (",self.dinheiro, "centavos) é insuficiente. Preco do Ticket:", self.preco ,"centavos")


