my_tuple =()

print(my_tuple)

my_tuple = (1, 'dos', True)

print(my_tuple[0])
print(my_tuple[1])

# my_tuple[0] = 2 -> TypeError: 'tuple' object does not support item assignment

my_tuple =(1)
print(type(my_tuple))


my_tuple =(1,)
print(type(my_tuple))


my_other_tuple =(2,3,4)
my_tuple += my_other_tuple
print(my_tuple)

x, y, z = my_other_tuple
print(x, y, z)

def coordenadas():
    return (5,4)

coordenada = coordenadas()
print(coordenada)

x,y = coordenadas()
print(x,y)