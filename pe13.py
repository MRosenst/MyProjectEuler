def addLargeNums(a, b):
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    
    if len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a

    largeSum = ''
    carry = 0
    for (i,j) in list(zip(a,b))[::-1]:  # [::-1] reverses the list
        digitSum = int(i) + int(j) + carry
        carry = digitSum // 10
        newDigit = digitSum % 10

        largeSum += str(newDigit)

    if carry != 0:
        largeSum += str(carry)[::-1]

    return largeSum[::-1]
        
def main():
    with open('pe13.txt', 'r') as f:
        largeNums = map(lambda n: n.strip(), f.readlines())
    
    total = ''
    for num in largeNums:
        total = addLargeNums(total, num)

    print(total)

if __name__ == '__main__':
    main()
