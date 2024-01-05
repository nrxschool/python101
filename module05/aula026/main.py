class Produto:
    def __init__(self, nome: str, quantidade_em_estoque: int, preco: float) -> None:
        self.nome = nome
        self.quantidade_em_estoque = quantidade_em_estoque
        self.preco = preco

    def esta_disponivel(self):
        return self.quantidade_em_estoque > 0

    def vender(self):
        self.quantidade_em_estoque = self.quantidade_em_estoque - 1
        # self.quantidade_em_estoque -= 1

    def __repr__(self) -> str:
        return f"Produto({self.nome}, está diponivel: {self.esta_disponivel()})"

    def __eq__(self, __value: "Produto") -> bool:
        return self.nome == __value.nome



microfone = Produto("Microfone", 20, 1200.70)
mouse = Produto("Microfone", 2, 250.99)

print(microfone == mouse)
