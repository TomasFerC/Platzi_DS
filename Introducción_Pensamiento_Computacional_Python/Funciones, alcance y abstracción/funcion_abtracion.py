def suma(a,b):
    total = a+b
    return total

print(suma(2,4))

def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        return f"{apellido} {nombre}"
    else:
        return f"{nombre} {apellido}"
print(nombre_completo("David", "Fernandez"))
print(nombre_completo("David", "Fernandez", inverso=True))
print(nombre_completo(nombre="David", apellido="Fernandez"))