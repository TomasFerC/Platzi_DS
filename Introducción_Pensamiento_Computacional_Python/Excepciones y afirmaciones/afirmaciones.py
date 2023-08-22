def primera_letra(lista_palabras):
    primeras_letras = []
    
    for palabra in lista_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es String'
            assert len(palabra) > 0 , 'No se permiten str vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(f"Error: {e}")

    return primeras_letras


palabras = ["Hola", "Mundo", "Python", '']
print(primera_letra(palabras))