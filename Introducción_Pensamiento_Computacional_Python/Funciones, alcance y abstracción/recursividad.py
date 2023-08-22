import sys
def factorial(numero):
    """Calcula el factorial de numero

    Args:
        numero (int): entero > 0
    Returns:
        int: numero!
    """
    print(numero)
    if numero == 1:
        return 1
    return numero * factorial(numero-1)

n = int(input("Escribe un entero: "))
print(factorial(n))

print(sys.getrecursionlimit())