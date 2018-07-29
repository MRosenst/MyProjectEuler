import csv

with open('pe22.txt', 'r') as f:
    names = f.read()

parser = csv.reader([names])
namelist = list(parser)[0]
namelist = sorted(namelist)

wordVal = lambda w: sum([ord(c) - ord('A') + 1 for c in w])

total = 0
for i in range(len(namelist)):
    total += (i + 1) * wordVal(namelist[i])

print(total)
