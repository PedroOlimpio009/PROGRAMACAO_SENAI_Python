class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        """Exibe os detalhes do produto."""
        print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades")

    def preco_final(self):
        """Retorna o preço do produto (sem alterações para o Produto base)."""
        return self.preco

    def emitir_nota(self):
        """Emite uma nota fiscal genérica para o produto."""
        print(f"Nota gerada para {self.nome}.")

    def repor(self, quantidade):
        """Repor estoque do produto."""
        self.estoque += quantidade
        print(f"Estoque de {self.nome} reposicionado. Novo estoque: {self.estoque} unidades.")

    def vender(self, quantidade):
        """Realiza a venda de uma quantidade de produtos, não permitindo vender mais do que o estoque."""
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"{quantidade} unidades de {self.nome} vendidas. Estoque atual: {self.estoque} unidades.")
        else:
            print(f"Não há estoque suficiente para vender {quantidade} unidades de {self.nome}.")
