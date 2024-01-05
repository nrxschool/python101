class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def comer(self):
        print(f"{self.nome} Comendo: 🍖")


class Cachorro(Animal):
    def latir(self):
        print(f"🐕 {self.nome} diz: Au Au")

class Gato(Animal):
    def miar(self):
        print(f"🐈 {self.nome} diz: Miau")


italia = Cachorro("Ítalia")
canada = Gato("Canadá")

italia.latir()
canada.miar()


italia.comer()
canada.comer()