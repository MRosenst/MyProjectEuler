def collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1

        count += 1

    return count

def main():
    largestCount = 0
    largestNum = 0
    for n in range(1000000, 1, -1):
        count = collatz(n)

        if count > largestCount:
            largestCount = count
            largestNum = n

            print(str(n) + ':\t' + str(count))

    print(largestNum)
    print(largestCount)

if __name__ == '__main__':
    main()
