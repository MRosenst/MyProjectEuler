from math import log

convert = lambda a, b: b * log(a)

values = []

for a in range(2, 101):
    for b in range(2, 101):
        values.append((a** b))

print(len(set(values)))
