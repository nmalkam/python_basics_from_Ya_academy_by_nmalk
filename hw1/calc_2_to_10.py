def my_func(x):
    sum = 0
    length = len(x)
    for num in x:
        sum += int(num) * 2 ** (length - 1)
        length -= 1
    print(sum)
    return sum


assert my_func('110') == 6
assert my_func('10010010') == 146


def main():
    x = input()
    print(my_func(x))


if __name__ == '__main__':
    main()
# 1102 = (1*22 + 1*21 + 0*20)10 = 610
# 100100102 = (1*27 + 0*26 + 0*25 + 1*24 + 0*23 + 0*22 + 1*21 + 0*20)10 = 14610
