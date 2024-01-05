class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def eh_de_maior(self):
        return self.idade >= 18
    



lucas: Pessoa = Pessoa("lucas", 26)
joao: Pessoa = Pessoa("joao", 6)

print(lucas.eh_de_maior())
lucas.idade = 35

print(lucas.idade)
