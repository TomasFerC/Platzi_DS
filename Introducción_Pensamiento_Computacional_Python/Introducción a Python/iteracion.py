# while

contador = 0

while contador < 10:
    print(contador)
    contador+=1

contador_externo = 0
contador_interno = 0
while contador_externo < 5:
    while contador_interno <6:
        print(contador_externo,contador_interno)
        contador_interno +=1

        if contador_interno >= 3:
            break

    contador_externo +=1
    contador_interno = 0

# for
frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
    print(fruta)

estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)

for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)