import random
import numpy as np

# Función para generar primos usando la criba de Eratóstenes
def criba(n):
    not_primes = set()

    # Bucle principal para encontrar números primos
    for i in range(2, int(n**0.5) + 1):
        if i in not_primes:
            continue  # Si el número está marcado como no primo, saltar

        # Marcar todos los múltiplos de i como no primos, empezando desde i * i
        for j in range(i * i, n + 1, i):
            not_primes.add(j)

    # Generar la lista de primos como los números que no están en not_primes
    primes = [i for i in range(2, n + 1) if i not in not_primes]

    return primes

# Función para verificar si un número es primo y encontrar sus divisores primos
def is_prime(n):
    if n < 2:
        return False

    # Generar lista de primos hasta raíz de n
    primes = criba(int(n**0.5) + 1)

    # Verificar si n es divisible por algún primo y recolectar todos los divisores
    divisors = [primeNumber for primeNumber in primes if n % primeNumber == 0]

    if len(divisors) > 0:
        return False  # n no es primo

    return True

print(is_prime(52))

# Función para generar un número primo aleatorio
def generar_primo(a, b):
    lista_primos = []
    # Generar un número primo aleatorio entre a y b
    for i in range(a, b):
        if is_prime(i):
            lista_primos.append(i)
    if len(lista_primos) == 0:
        return None
    else:
        return random.choice(lista_primos)
    
print(generar_primo(90, 96))

# Función para encontrar el máximo común divisor de dos números
def mcd(a, b):
    # Inicializamos la lista de factores
    factores = []

    if a == 0 or b == 0:
        return None, factores

    if a > b: # Si a es mayor que b
        r = a % b
        while r != 0:
            r = a % b
            x = int(a / b)
            a = b
            b = r
            factores.append(x)
        return a, factores
    elif b > a: # Si b es mayor que a
        r = b % a
        while r != 0:
            r = b % a
            x = int(b / a)
            b = a
            a = r
            factores.append(x)
        return b, factores
    elif a == b: # Si a es igual a b
        for i in range(1, a + 1):
            if a % i == 0:
                factores.append(i)
        return a, factores
    
    return None, factores

print(mcd(0,54))

# Función para encontrar el inverso modular de un número e en módulo n
def inverso_modular(e, n):

    # Verificar si el máximo común divisor de e y n es 1
    mcd_, factores = mcd(e, n)

    # Si el mcd no es 1, no hay inverso modular
    if mcd != 1:
        return None
    
    # Inicializar las variables

    

print(inverso_modular(3, 12))