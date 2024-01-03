import math

# Funções Básicas
print("Hello, World!")
user_input = input("Digite algo: ")
print("Você digitou:", user_input)
print("Tamanho da string digitada:", len(user_input))

# Conversão de Tipos
numero = int("10")
ponto_flutuante = float("10.5")
booleano = bool(1)
lista = list("abcd")
tupla = tuple("abcd")
dicionario = dict(a=1, b=2)
conjunto = set([1, 2, 3])

# Funções Matemáticas
raiz_quadrada = math.sqrt(16)
potencia = math.pow(2, 3)
exponencial = math.exp(1)
logaritmo = math.log(10)
seno = math.sin(math.pi / 2)
cosseno = math.cos(0)
tangente = math.tan(math.pi / 4)

# Funções de Manipulação de Strings
texto = "Python é incrível"
texto_maiusculas = texto.upper()
texto_minusculas = texto.lower()
lista_palavras = texto.split()
texto_juntado = " ".join(lista_palavras)
texto_substituido = texto.replace("incrível", "fantástico")

# Funções para Trabalhar com Listas
lista_numeros = [1, 2, 3, 4]
lista_numeros.append(5)
lista_numeros.remove(2)
ultimo_item = lista_numeros.pop()
lista_numeros.reverse()
lista_numeros.sort()

# Outras Funções Úteis
for indice, valor in enumerate(lista_numeros):
    print(f"Índice: {indice}, Valor: {valor}")

# Funções de Tratamento de Exceções
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
finally:
    print("Bloco finally executado.")

# Imprimindo resultados
print("Número:", numero)
print("Ponto Flutuante:", ponto_flutuante)
print("Booleano:", booleano)
print("Lista:", lista)
print("Tupla:", tupla)
print("Dicionário:", dicionario)
print("Conjunto:", conjunto)
print("Raiz Quadrada:", raiz_quadrada)
print("Potência:", potencia)
print("Exponencial:", exponencial)
print("Logaritmo:", logaritmo)
print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)
print("Texto em Maiúsculas:", texto_maiusculas)
print("Texto em Minúsculas:", texto_minusculas)
print("Lista de Palavras:", lista_palavras)
print("Texto Juntado:", texto_juntado)
print("Texto Substituído:", texto_substituido)
print("Lista após operações:", lista_numeros)
print("Último item removido:", ultimo_item)
