# simple_num_3
# 2.3. Cycles N_v4

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def simple_num_3():
    n = int(input())
    # entrings = []
    count = 0
    res = 0
    while count != n:
        if is_prime(int(input())):
            res += 1
        # entrings.append(int(input()))
        count += 1
    return res
    # if num == 1:
    #     return "NO"
    # for i in range(2, (num // 2) + 1):
    #     if num % i == 0:
    #         return "NO"
    # return "YES"


# assert simple_num_3() == "512345"
# assert simple_num_3() ==
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    print(simple_num_3())


if __name__ == '__main__':
    main()
