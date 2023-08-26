import random

def busqueda_lineal(lista, objetivo):
    """Esta funcion busca el elemento objetivo dentro de lista

    Args:
        lista (list): lista de numero enteros
        objetivo (int): es un numero entero

    Returns:
        bool: True si lo enccuentra el la lista, sino False
    """
    # iniciamos match como False
    match = False # O(1)

    #buscamos con for el objetivo en la lista
    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    # Input nos indicara el tamaño de la lista
    tamanio_de_lista = int(input('De que tamaño sera la lista? '))
    # Input del objetivo a buscar
    objetivo = int(input('Que numero quieres encontrar? '))

    # Generamos una lista del tamaño indicada en tamanio_de_lista
    lista = [random.randint(0,100) for i in range(tamanio_de_lista)]
    
    #Se genera variable con valor True o False dependiendo sie enuntra o no el objetvio
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
