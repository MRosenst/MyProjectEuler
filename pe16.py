def digitSum(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10

    return res

def main():
    print(digitSum(2**1000)) 


if __name__ == '__main__':
    main()
