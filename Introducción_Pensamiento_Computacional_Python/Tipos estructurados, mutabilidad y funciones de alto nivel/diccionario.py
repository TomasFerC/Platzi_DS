my_dict = {
    'David':35,
    'Erika': 32,
    'Jaime': 50 
}

print(my_dict['David'])

print(my_dict.get('David',None))
print(my_dict.get('Juan',None))

my_dict['David']=12
print(my_dict)
my_dict['Juan']=18
print(my_dict)

del my_dict['Juan']
print(my_dict)

for llave in my_dict.keys():
    print(llave)

for llave in my_dict:
    print(llave)

for valor in my_dict.values():
    print(llave)

for llave,valor in my_dict.items():
    print(llave,valor)

print('Juan' in my_dict)
print('Jaime' in my_dict)

# Retos dict comprehension

mi_dict  = { numero : numero*2 for numero in range(100) }
print(mi_dict)

mi_dict  = { x : y*2 for x,y in my_dict.items() }
print(mi_dict)