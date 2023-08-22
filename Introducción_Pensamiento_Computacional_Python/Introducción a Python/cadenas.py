cadena = '123'
multplicacion_cadena = cadena * 3
print(multplicacion_cadena)

concatenar = cadena + '456'
print(concatenar)

mezclar_operadores = ('Hip' * 3) + 'hurra'
print(mezclar_operadores)

cadena_de_formato = f"{'Hip' * 3} hurra"
print(cadena_de_formato)

#Funciones sobre string

my_str = "Tomas"

## Longitud de str
print(len(my_str))

## Indexing
print(my_str[0])
print(my_str[2])

## Slicing
print(my_str[2:])
print(my_str[:3])
print(my_str[:-3])
print(my_str[::2])

# Entradas
nombre = input("Cual es tu nombre: ")
numero_str = input("Escribe un numero: ")
numero_int = int(input('Escribe un numero: '))
print(type(numero_str))
print(type(numero_int))

# Print con Entradas
print("Tu nombre es", nombre)
print(f"Tu nombre es {nombre}")

# Reto
nombre_usuario = input("Cual es tu nombre: ")
print(f'El nombre del usuario es {nombre_usuario}, el largo del nombre es {len(nombre_usuario)}')
