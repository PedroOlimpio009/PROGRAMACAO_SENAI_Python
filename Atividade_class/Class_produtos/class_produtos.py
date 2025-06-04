class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def comprar(self, qtd):
        if qtd <= self.estoque:
            self.estoque -= qtd
        else:
            print(f"Estoque insuficiente! Disponível: {self.estoque}")
    def repor(self, qtd):
        self.estoque += qtd
    def mostrar_estoque(self):
        print(f"Estoque atual de {self.nome}: {self.estoque}")

