def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def sumOfDigits(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res
