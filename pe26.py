def recurrance(x):
    asStr = str(x).split('.', 2)[1]
    for i,d in enumerate(asStr):
        if d in asStr[:i]:
            return i - asStr.index(d)

    return 1

recurrances = [recurrance(1/x) for x in range(1,1000)]

for x in range(1,1000):
    print(str(x) + ' ---\t' + str(1/x) + ' ---\t' + str(recurrances[x+1]))
