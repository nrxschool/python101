dicionario = {
    "key": "value",
    "nome": "Lucas",
    "idade": 26,
    "casado": True
}

impares = [
    i
    for i in range(10)
    if i % 2 != 0
]

pares = [
    i
    for i in range(10)
    if i % 2 == 0
]


novo = {
    impar: par
    for (impar, par) in zip(impares, pares)
}

print(novo)