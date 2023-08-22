# # Operadores de comparación
# print(2==3)
# print(2!=3)
# print(2<3)
# print(2>3)
# print(2<=3)
# print(2>=3)

# # Operadores lógicos
# print(5==5 and 5>3)
# print(2==3 or 2<3)
# print(not 2==3)

# Coparacion de dos enteros
num_1 = int(input('Escoge un entero: '))
num_2 = int(input('Escoge otro entero: '))

if num_1 > num_2:
    print(f'El numero {num_1} es mayor que {num_2}')
elif num_1 < num_2:
    print(f'El numero {num_2} es mayor que {num_1}')
else:
    print(f'Los numeros {num_2} y {num_1} son iguales')

# Reto escribe un programa que compare la edades de dos usuarios y diga quien es mayor que quien

# Input del usuario para la primera persona
nombre_1 =input("Indique su nombre: ")
edad_1 =int(input('Ingrese su edad: '))

# Input del usuario para la segunda persona
nombre_2 = input("Indique su nombre: ")
edad_2 = int(input('Ingrese su edad: '))

# Comparación de edades y resultados
if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}.')
elif edad_1 < edad_2:
    print(f'{nombre_2} es mayor que {nombre_1}.')
else:
    print(f'{nombre_2} y {nombre_1} tienen la misma edad.')
