"""
    Realizaremos busqueda binaria 
"""
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    """Hace una busqueda binaria de un objetivo en una lista ordenada.

    Args:
        lista (list): lista de enteros
        comienzo (int): primer numero de la lista
        final (_type_): ultimo numero de la lista
        objetivo (_type_): entero a buscar

    Returns:
        bool: Dependiendo si encuentra o nos da True, False o llama nuevamente a busqueda bianria.
    """
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final,objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1,objetivo)

if __name__ == '__main__':
    # Input nos indicara el tamaño de la lista
    tamanio_de_lista = int(input('De que tamaño sera la lista? '))
    # Input del objetivo a buscar
    objetivo = int(input('Que numero quieres encontrar? '))

    # Generamos una lista del tamaño indicada en tamanio_de_lista, la cual es ordenada son sorted
    lista = sorted([random.randint(0,100) for i in range(tamanio_de_lista)])

    #Se genera variable con valor True o False dependiendo sie enuntra o no el objetvio
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
