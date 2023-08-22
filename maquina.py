class MaquinaDeVendas:
    def __init__(self,preco):
        self.preco = preco
        self.dinheiro = 0
        self.total=0

    def inserir_dinheiro(self,valor):
        self.dinheiro = self.dinheiro + valor

    def imprimir_ticket(self):
        if(self.dinheiro>=self.preco):
            print(f"""####################
       TICKET
    {self.preco} centavos""")

            if(self.dinheiro>self.preco):
                troco = self.dinheiro - self.preco
                print(f"Troco:{troco} centavos")
            print("####################")
            self.total = self.total + self.preco
            self.dinheiro = 0

        else:
            print("O dinheiro inserido na máquina (",self.dinheiro, "centavos) é insuficiente. Preco do Ticket:", self.preco ,"centavos")


