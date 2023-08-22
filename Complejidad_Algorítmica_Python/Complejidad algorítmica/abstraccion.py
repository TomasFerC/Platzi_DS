def f(x):
    respuesta = 0

    for i in range(1000):
        respuesta += 1
    
    for i in range(x):
        respuesta += 1
    
    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1
    return respuesta

if __name__ == '__main__':
    n = 10000

    print(f(n))