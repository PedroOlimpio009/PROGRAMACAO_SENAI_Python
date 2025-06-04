from produto import Produto
def main():
    # Criando alguns produtos
    p1 = Produto("Teclado", 100.0, 20)
    p2 = Produto("Mouse", 50.0, 30)

    # Exibindo detalhes
    p1.exibir_detalhes()
    p2.exibir_detalhes()

    # Emitindo notas fiscais
    p1.emitir_nota()
    p2.emitir_nota()

    # Calculando preço final (sem alterações para o Produto base)
    print(f"Preço final de {p1.nome}: R${p1.preco_final()}")
    print(f"Preço final de {p2.nome}: R${p2.preco_final()}")

    # Repondo estoque
    p1.repor(10)

    # Vendendo produtos
    p2.vender(5)
    p1.vender(50)  # Vai tentar vender mais do que o estoque disponível, então vai dar erro

if __name__ == "__main__":
    main()
