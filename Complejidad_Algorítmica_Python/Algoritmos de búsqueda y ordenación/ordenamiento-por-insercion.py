import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice
        
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista

if __name__ == '__main__':
    # Input nos indicara el tamaño de la lista
    tamanio_de_lista = int(input('De que tamaño sera la lista? '))

    # Generamos una lista del tamaño indicada en tamanio_de_lista
    lista = [random.randint(0,100) for i in range(tamanio_de_lista)]
    
    # Insertar la lista ordenada por la funcion ordenamiento_por_insercion, en la variable lista_ordenada
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(f"""
    Lista antes de ordenar:
    {lista}
    """)
    print(f"""
    Lista ordenada:
    {lista_ordenada}
    """)
