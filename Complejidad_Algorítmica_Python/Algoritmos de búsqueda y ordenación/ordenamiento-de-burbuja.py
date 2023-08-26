import random

def ordenamiento_de_burbuja(lista):
    largo_lista = len(lista)
    
    for n in range(largo_lista):
        for j in range(0, largo_lista- n - 1):
            
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

if __name__ == '__main__':
    # Input nos indicara el tamaño de la lista
    tamanio_de_lista = int(input('De que tamaño sera la lista? '))

    # Generamos una lista del tamaño indicada en tamanio_de_lista, la cual es ordenada son sorted
    lista = [random.randint(0,100) for i in range(tamanio_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)