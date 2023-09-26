def toddler_calc(n, m):
    n = str(input())[::-1]
    m = str(input())[::-1]
    index = 0
    print(len(n))
    out = ''
    if n >= m:
        x = n
        y = m
    else:
        x = m
        y = n
    for _ in range(len(x) - 1):
        num_summed = str((int(n[_]) + int(m[_])) % 10)
        out = out + num_summed
        index += 1
    # print(y[index:])
    k = str(y[index:])[::-1]
    # print(k)

    # out_s = y[index:]
    # out_s = str(y[index:])
    # print(y[index:])
    # print(out_s)
    out = out[::-1]
    # print(out)
    # print(f'{out}{k}')
    out_k = k + out
    digits = ''.join([c for c in out_k if c.isdigit()])
    print(digits)


assert toddler_calc(123, 99) == 112
assert toddler_calc(5, 5) == 0
assert toddler_calc(405, 839) == 234


def main():
    n = str(input())[::-1]
    m = str(input())[::-1]
    print(toddler_calc(n, m))


if __name__ == '__main__':
    toddler_calc()



