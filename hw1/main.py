def roots(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    if a == 0:
        if c ** 2 == b:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'
    x = (c ** 2 - b) / a
    if x.is_integer():
        return int(x)
    else:
        return 'NO SOLUTION'


assert roots(9, 16, 7) == "NO SOLUTION"
assert roots(1, 0, 0) == 0
assert roots(1, 2, 3) == 7
assert roots(1, 2, -3) == "NO SOLUTION"


def main():
    a, b, c = [int(input())for _ in range(3)]

    # a = int(input())
    # b = int(input())
    # c = int(input())
    print(roots(a, b, c))


if __name__ == '__main__':
    main()




