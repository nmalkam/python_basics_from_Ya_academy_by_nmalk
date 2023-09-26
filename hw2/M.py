def my_func(num_a, num_b, num_c):
    def dic(num):
        numMap = {}
        # for item in range(len(num)):
        for item in num:
            numMap[int(num[item])] = item
        print(numMap)
        # return numMap
    dic_num_a = {}
    dic_num_b = {}
    dic_num_c = {}
    dic_num_a = dic(num_a)
    # n = len(num_a)



    # for index in range(len(num_a)):
        # if key_of_dic in
            #which is 1
        # return num

assert my_func(12, 13, 14) == 1
assert my_func(23, 13, 63) == 3
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    print(my_func(num_a, num_b, num_c))


if __name__ == '__main__':
    main()
