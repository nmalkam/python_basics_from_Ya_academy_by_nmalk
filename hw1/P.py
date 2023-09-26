def time_for_delivery(x, b, c):
    # time = abs(x - b) / c
    # print(f'{float(abs(x - b) / c):.{2}f}')
    return f'{float(abs(x - b) / c):.2f}'


assert time_for_delivery(10, 32, 5) == 4.40
assert time_for_delivery(1, 100, 30) == 3.30


def main():
    x = int(input())
    b = int(input())
    c = int(input())
    print(time_for_delivery(x, b, c))


if __name__ == '__main__':
    main()
# a = 2
# >>> n = 3
# >>> f'{a:.{n}f}'
# '2.000'
f'{():.{2}f}'
