# Pueden ser vacias
lista_1 = []
print(lista_1)

# Con un elemento
lista_2 = ["Isabel"]
print(lista_2)

# Varios elementos
lista_3 = ["Isabel", "Juan"]
print(lista_3)

# Distintos tipos de elementos
lista_4 = ["Isabel", 2, True]
print(lista_4)

# Lista con listas dentro
lista_5 = ["Isabel", [1, 2, 3]]
print(lista_5)

fruits = []

# .append para agregar
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melon")
print(fruits)

# Puedo ordenar con .sort
fruits.sort()
print(fruits)  # -> en este caso por orden alfabetico

# Podemos elminar con .pop que a demas devuleve el elemtno eliminado podemos guardar en una varibale
print(fruits.pop())
print(fruits.pop(1))

# Podemos insertar en una posision con .insert
fruits.insert(1, "Apple")
fruits.insert(0, "Strawberry")
print(fruits)

# Remover con .remove si no esta salta un Value Error
try:
    fruits.remove("Kiwi")
except ValueError as e:
    print(f"Error: {e}")
