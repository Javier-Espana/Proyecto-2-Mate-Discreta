import random

# Función para generar números primos usando la criba de Eratóstenes
def criba(n):
    not_primes = set()
    for i in range(2, int(n**0.5) + 1):
        if i in not_primes:
            continue
        for j in range(i * i, n + 1, i):
            not_primes.add(j)
    return [i for i in range(2, n + 1) if i not in not_primes]

# Verifica si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Genera un número primo aleatorio dentro de un rango
def generar_primo(a, b):
    primos = [x for x in range(a, b + 1) if is_prime(x)]
    return random.choice(primos) if primos else None

print(generar_primo(90, 96)) # None

# Genera las llaves pública y privada para RSA
def generar_llaves(rango_inferior, rango_superior):
    p = generar_primo(rango_inferior, rango_superior)
    q = generar_primo(rango_inferior, rango_superior)
    while q == p:  # Asegurarse de que p y q sean distintos
        q = generar_primo(rango_inferior, rango_superior)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.choice([x for x in range(2, phi) if mcd(x, phi) == 1])
    d = inverso_modular(e, phi)

    # Asegurarse de que e y d sean distintos
    attempts = 0
    while e == d and attempts < 100:
        e = random.choice([x for x in range(2, phi) if mcd(x, phi) == 1])
        d = inverso_modular(e, phi)
        attempts += 1

    if e == d:
        return None  # No se pudieron generar llaves distintas

    return (e, n), (d, n)

# Algoritmo de Euclides para el máximo común divisor
def mcd(a, b):
    # Programación defensiva: asegurar que los inputs sean enteros positivos
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Ambos números deben ser enteros.")
    if a <= 0 or b <= 0:
        raise ValueError("Ambos números deben ser positivos.")

    # Asegurar que a >= b
    if b > a:
        a, b = b, a

    # Algoritmo de Euclides
    while b:
        a, b = b, a % b
    return a

print(mcd(54, 24)) # 6
print(mcd(17, 31)) # 1

# Algoritmo extendido de Euclides para encontrar el inverso modular
def inverso_modular(e, n):
    t, new_t = 0, 1
    r, new_r = n, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:  # No existe inverso modular
        return None
    if t < 0:
        t += n
    return t

print(inverso_modular(3, 11))  # 4
print(inverso_modular(7, 40))  # 23

# Encripta un número usando la llave pública
def encriptar(mensaje, llave_publica):
    e, n = llave_publica
    if mensaje < 0 or mensaje >= n:
        raise ValueError("El mensaje debe ser un número positivo menor que n")
    return ((mensaje ** e) % n)

print(encriptar(42, (7, 221))) # 185

# Desencripta un número usando la llave privada
def desencriptar(cifrado, llave_privada):
    d, n = llave_privada
    return (cifrado ** d) % n

print(desencriptar(185, (103, 221))) # 42

"""
# Menú interactivo para el sistema RSA
def menu():
    while True:
        print("\n--- Menú RSA ---")
        print("1. Establecer rango para generar primos")
        print("2. Generar llaves RSA")
        print("3. Encriptar mensaje")
        print("4. Desencriptar mensaje")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            global rango_inferior, rango_superior
            rango_inferior = int(input("Ingrese el rango inferior: "))
            rango_superior = int(input("Ingrese el rango superior: "))
            if rango_superior <= 2:
                print("El rango superior debe ser mayor que 2. Intente de nuevo.")
            else:
                print(f"Rango establecido de {rango_inferior} a {rango_superior}")
        elif opcion == "2":
            if 'rango_inferior' not in globals() or 'rango_superior' not in globals() or rango_superior <= 2:
                print("Primero debe establecer un rango válido para generar primos.")
                continue
            print("Generando llaves...")
            global llave_publica, llave_privada
            llave_publica, llave_privada = generar_llaves(rango_inferior, rango_superior)
            print(f"Clave pública: {llave_publica}")
            print(f"Clave privada: {llave_privada}")
        elif opcion == "3":
            if 'llave_publica' not in globals():
                print("Primero debe generar las llaves RSA.")
                continue
            mensaje = int(input("Ingrese el mensaje a encriptar (número): "))
            cifrado = encriptar(mensaje, llave_publica)
            print(f"Mensaje encriptado: {cifrado}")
        elif opcion == "4":
            if 'llave_privada' not in globals():
                print("Primero debe generar las llaves RSA.")
                continue
            cifrado = int(input("Ingrese el mensaje encriptado (número): "))
            desencriptado = desencriptar(cifrado, llave_privada)
            print(f"Mensaje desencriptado: {desencriptado}")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Pruebas del sistema RSA
def main():
    rango_inferior = 50
    rango_superior = 100

    print("Generando llaves...")
    llave_publica, llave_privada = generar_llaves(rango_inferior, rango_superior)
    print(f"Clave pública: {llave_publica}")
    print(f"Clave privada: {llave_privada}")

    mensajes = [42, 89, 75]
    for mensaje in mensajes:
        print(f"\nMensaje original: {mensaje}")
        cifrado = encriptar(mensaje, llave_publica)
        print(f"Mensaje encriptado: {cifrado}")
        desencriptado = desencriptar(cifrado, llave_privada)
        print(f"Mensaje desencriptado: {desencriptado}")

if __name__ == "__main__":
    main()
    menu()
    """

