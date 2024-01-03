idade = input("Qual sua idade? ")
nome = input("Qual seu nome? ")

idade = int(idade)

if idade > 18 and nome == "Lucas":
    print("Aprovado")
else:
    print("Reprovado")