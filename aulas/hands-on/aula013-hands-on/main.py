def hello():
    print("Olá")


def world():
    hello()
    print("Mundo")


world()


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


def soma(a,b):
    return a+b

