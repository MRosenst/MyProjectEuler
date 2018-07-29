from fractions import gcd

def calcQuadratic(a, b):
    return lambda n: n * n + a * n + b


def isPrime(p):
    b = 2
    while b * b <= p:
        if p % b == 0:
            return False
        b += 1
    return True


def numOfPrimes(a,b):
    print(a,b)
    
    n = 0

    while isPrime(calcQuadratic(a,b)(n)): 
        n += 1

    print(n)
    return n


def main():
    primeCounts = []
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primeCounts.append((numOfPrimes(a,b), a, b))
            print(a,b)

    print(max(primeCounts))


if __name__ == '__main__':
    main()


