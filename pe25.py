def numOfDigits(n):
    num = 0
    while n > 0:
        n //= 10
        num += 1
    
    return num

def fib(lim):
    fib1 = 1
    fib2 = 1

    i = 2

    while numOfDigits(fib2) < lim:
        # perform a pseudo-swap
        fib2 = fib1 + fib2
        fib1 = fib2 - fib1
        i += 1

    return i

print(fib(1000))
