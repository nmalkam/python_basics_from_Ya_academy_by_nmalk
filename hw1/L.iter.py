from itertools import zip_longest
a = list(map(int, input('a = ')))
b = list(map(int, input('b = ')))
sum = ''.join(reversed([str((x + y) % 10) for x, y in zip_longest(reversed(a), reversed(b), fillvalue=0)]))
print(sum)
