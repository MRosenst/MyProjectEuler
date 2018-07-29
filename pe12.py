# Python3 implementation of Naive method 
# to count all divisors
 
import math
 
# function to count the divisors
def countDivisors(n) :
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
             
            # If divisors are equal,
            # count only one
            if (n / i == i) :
                cnt = cnt + 1
            else : # Otherwise count both
                cnt = cnt + 2
                 
    return cnt

triangle = lambda n: n * (n + 1) / 2

def triangleFindDivisors(bound):
    n = 1
    while countDivisors(triangle(n)) < bound:
        n += 1
    return triangle(n)

print(triangleFindDivisors(500))
