from math import gcd

product_num = 1
product_denom = 1

for a in range(10,50):
    for b in range(10,1000):
        if a == b:
            continue

        a0 = int(str(a)[0])
        a1 = int(str(a)[1])
        b0 = int(str(b)[0])
        b1 = int(str(b)[1])
        if a1 == 0 or b1 == 0:
            continue

        if a0 == b1 and a1 * b == b0 * a:
            print(a,b)
            product_num *= a
            product_denom *= b
        if a1 == b0 and a0 * b == b1 * a:
            print(a,b)
            product_num *= a
            product_denom *= b
        
print('Result is: {}'.format(product_denom // gcd(product_num, product_denom)))
        
