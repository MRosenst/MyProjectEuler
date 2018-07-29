def divisors(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)

    return div

abundant = lambda n: sum(divisors(n)) > n
abundantNums = list(filter(abundant, range(1, 28124)))

print('Made list of abundants')
print(abundantNums[:5])
abundantSet = set(abundantNums)

print('Converted list into set')

def isNotSumOf2Abundants(n):
    isSum = False
    for a in abundantSet:
        if n - a in abundantSet:
            isSum = True

    if not isSum:
        print(n)

    return not isSum

print(sum(list(filter(isNotSumOf2Abundants, range(1, 28127)))))
