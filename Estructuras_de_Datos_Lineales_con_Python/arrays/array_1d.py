import random


class Array:
    """
    Estea clase es la representacion de un arrey
    """

    def __init__(self, capacity, fill_value=None):
        """
        capacity: es un entero que indica la capacidad o tamaño
        fill_value: Valor con el que vamos a rellenar. Defaults to None.
        """
        # Los elementos van a hacer guardados en una lista vacia
        self.items = list()

        # El ciclo es para darle el valor (fill_value) a los elementos. esto le da valores por defectos.
        for i in range(capacity):
            self.items.append(fill_value)

    # Esto es un metodo provado para consulta, no se modifica, sirve para ver el tamaño del array.
    def __len__(self):
        return len(self.items)

    # Sirve para ver como string los elmentos.
    def __str__(self):
        return str(self.items)

    # Es un metodo para recorrer estructura
    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        """Sirve para obtener o retornar el elemento en un indixe del array

        Args:
            index (int): es el indice que buscaremos
        """
        return self.items[index]

    def __setitem__(self, index, new_item):
        """Sirve para poder cambiar un elemento en el indice que le pasamos, por el atributo nuevo.

        Args:
            index (int): es el indice que buscaremos
            new_item: elemento que remplaza el elemento acual en el indice pasado
        """
        self.items[index] = new_item


class Array_2(Array):
    # Modifica cada elemento del array por un entero aleatorio del 0 al 100
    def __fillin__(self):
        for n in range(len(self.items)):
            self.items[n] = random.randint(0, 100)

    # En el caso de contener numero entero los sumara
    def __sum__(self):
        try:
            # return sum(self.items)
            suma = 0
            for i in self.items:
                suma += i
            return suma
        except TypeError as error:
            return f"Error al sumar los elementos: {error}"
