def my_func(x, b):
    return x + int(b, 2)


# assert my_func(123, "1101") == 136
# assert my_func(783, "10110111") == 966


def main():
    x = int(input())
    b = input()
    print(my_func(x, b))


if __name__ == '__main__':
    main()
# decimal_number = int(binary_number, 2)
