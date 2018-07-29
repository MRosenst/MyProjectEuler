def largestVerticalSum(pyr, total, i, j):
    if i == len(pyr):
        return total

    return max(largestVerticalSum(pyr, total + pyr[i][j], i + 1, j),
                  largestVerticalSum(pyr, total + pyr[i][j], i + 1, j + 1))

def main():
    with open('pe18.txt', 'r') as f:
        txt = f.readlines()

    listInts = lambda string: list(map(int, string.strip().split(' ')))

    pyramid = list(map(listInts, txt))
    
    print(pyramid)

    print(largestVerticalSum(pyramid, 0, 0, 0))

if __name__ == '__main__':
    main()
