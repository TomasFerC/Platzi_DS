x = 0.0
for i in range(10):
    x += 0.1
    print(x)
if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')



# def binary(binary_num):
#     sums = 0.0
#     pos = 1
#     for i in binary_num:
#          if i == '1':
#             sums += round(1/(2**pos),10)
#          pos += 1 
#     return round(sums, 10)

# def main():
#     #ingresa solo los bits despues del punto y sin los tres puntos finales
#     bin_num = input('Give me the binary num: ')
#     result = binary(bin_num)
#     print(f'{bin_num}is {result}in decimal')

# if __name__ == '__main__':
#     main()


print((0.1 + 0.1 + 0.1) == 0.3)
print((round(0.1 + 0.1 + 0.1,1)) == 0.3)
print(round(0.3,1))
print(0.1 + 0.1 + 0.1)
print(round(0.1 + 0.1 + 0.1,1))

# Solucion 
x = 0.0
for i in range(10):
    x += 0.1
    x = round(x,1)
    print(x)

if x == 1.0:
    print(f'x = 1.0')
else:
    print(f'x != {x}')