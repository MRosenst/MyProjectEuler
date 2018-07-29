import inflect
p = inflect.engine()

word = ''
for i in range(1,1001):
    word += p.number_to_words(i)

word = filter(lambda c: c.isalpha(), word)
print(word)

print len(word)
