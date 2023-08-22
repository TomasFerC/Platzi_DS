
def divide_elemento_de_lista(lista, divisor):
    """Divide todos los elementos de una lista por el divisor.

    Args:
        lista (list): lista de numero
        divisor (int or float): un numero entero o flotante

    Returns:
        list: lista que contiene los lementos de una lista dividiso por un divisor
    """
    try:
        return [ i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista =list(range(10))
divisor = 0
print(divide_elemento_de_lista(lista, divisor))