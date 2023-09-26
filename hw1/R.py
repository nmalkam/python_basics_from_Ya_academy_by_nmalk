def my_func(x, cash):
    sum = 0
    length = len(x)
    for num in x:
        sum += int(num) * 2 ** (length - 1)
        length -= 1
    # print(cash - sum)
    # print(type(cash), type(sum))
    return cash - sum


# assert my_func('1001001', 100) == 27
# assert my_func('101111100', 500) == 120


def main():
    x = input()
    cash = int(input())
    print(my_func(x, cash))


if __name__ == '__main__':
    main()
# 1102 = (1*22 + 1*21 + 0*20)10 = 610
# 100100102 = (1*27 + 0*26 + 0*25 + 1*24 + 0*23 + 0*22 + 1*21 + 0*20)10 = 14610
