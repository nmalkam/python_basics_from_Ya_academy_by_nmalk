def my_func(num_children, num_candies):
    # full_num = num_candies // num_children
    # remainder = num_candies/full_num
    return str(num_candies // num_children, "\n", num_candies - ((num_candies // num_children)*num_children))
    # print(f"{num_candies // num_children} \n {num_candies - ((num_candies // num_children) * num_children)}")


assert my_func(3, 100) == 33, 1


def main():
    num_children = int(input())
    num_candies = int(input())
    print(my_func(num_children, num_candies))


if __name__ == '__main__':
    main()
