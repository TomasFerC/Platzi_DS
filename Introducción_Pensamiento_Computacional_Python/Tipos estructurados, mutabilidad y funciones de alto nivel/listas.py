my_list = [1,2,3]

print(my_list[0])

print(my_list[1:])

my_list.append(4)
print(my_list)

my_list[0] = 'a'
print(my_list)

print(my_list.pop())
print(my_list)

for element in my_list:
    print(element)

a = [1,2,3]
b = a
print(id(a) == id(b))

c = [a,b]
print(c)
print(a.append(5))
print(c)


# Como evitar?
a = [1,2,3]
b = a[:]
c = list(a)
print(id(a) == id(b))
print(id(a) == id(c))

c = [a,b]
print(c)
a.append(5)
print(c)


#List comprehension

my_list = list(range(100))

double = [ i * 2 for i in my_list]
print(double)

pares = [ i for i in my_list if i % 2 == 0 ]
print(pares)
