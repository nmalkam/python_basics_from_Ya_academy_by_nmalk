def my_funb(r, g, b):
    return r + b + 1


assert my_funb(1, 2, 1) == 3
assert my_funb(1, 100, 1) == 3
# assert my_funb(1, 2, 3) == 5
# assert my_funb(1, 2, 3) == 5
# assert my_funb(1, 2, 3) == 5


def main():
    r = int(input())
    g = int(input())
    b = int(input())
    print(my_funb(r, g, b))


if __name__ == '__main__':
    main()
