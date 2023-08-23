# O(n) + O(n) = O(n+n) = O(2n) => O(n), por que termino mayor es n, esto tiene un crecimiento lineal
def f(n):

    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n+n) = O(2n) => O(n), por que termino mayor es n, esto tiene un crecimiento lineal
def f2(n):

    for i in range(n):
        print(i)

    for i in range(n*n):
        print(i)

# O(n) * O(n) = O(n * n) => O(n**2), termino mas grande n**2, crecimiento cuadratico
def f3(n):

    for i in range(n):
        for j in range(n):
            print(i,j)

# O(2**n) crecimiento Polinomial
def f4(n):
    if n == 0 or n == 1:
        return 1
    return f4(n-1) + f4(n-2)

if __name__ == '__main__':
    n = 10000

    print(f(n))
    print(f2(n))
    print(f3(n))
    print(f4(n))
