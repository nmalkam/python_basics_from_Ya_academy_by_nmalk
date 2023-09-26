def my_func(x):
    return x


assert my_func(123) == 53
assert my_func(741) == 115
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    x = int(input())
    print(my_func(x))


if __name__ == '__main__':
    main()
