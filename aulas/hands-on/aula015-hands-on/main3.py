l = [1, 2, 3, 4]


def soma_4(x):
    return x + 4

list(map(soma_4, l))

def nosso_map(func, lista):
    nova = []
    for item in lista:
        x = func(item)
        nova.append(x)

    return nova

result = nosso_map(soma_4, l)

print(result)

