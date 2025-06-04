from class_produtos import Produto

# Exemplo de uso
produto = Produto("Caneta", 1.50, 100)
produto.mostrar_estoque()
produto.comprar(20)
produto.mostrar_estoque()
produto.comprar(100)  # Tentativa de compra além do estoque
produto.repor(50)
produto.mostrar_estoque()