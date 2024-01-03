lista = []

for i in range(100):
    if i > 50:
        lista.append(i)


# list comprehention
lista = [
    i
    for i in range(100)
    if i >50
]

print(lista)