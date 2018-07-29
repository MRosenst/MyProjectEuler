from operator import mul

def factorial(n):
    product = 1
    for i in range(2, n):
        product *= i

    return product


def main():
    n = 20
    print(factorial(2 * n) // (factorial(n)**2))

if __name__ == '__main__':
    main()
