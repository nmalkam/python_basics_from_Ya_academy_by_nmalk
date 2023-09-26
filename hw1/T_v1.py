def my_func(n_weight, m_price, k1_price, k2_price):
    # weight_k1, weight_k2 = 1,2
    # weight_map = {}
    for item in range(n_weight):
        weight_k1 = n_weight - item
        weight_k2 = ((m_price * n_weight) - (k1_price * weight_k1)) / k2_price
        # weight_k2 = item
        if weight_k2 % 1 == 0 and 0 < weight_k2 < weight_k1 and weight_k1 + weight_k2 == n_weight:
            # weight_map[weight_k1] = weight_k2
            # print(weight_k1, int(weight_k2))
            return str(f"{weight_k1} {int(weight_k2)}")
    # return weight_k1, weight_k2


assert my_func(32, 285, 300, 240) == "24 8"


def main():
    n_weight = int(input())
    m_price = int(input())
    k1_price = int(input())
    k2_price = int(input())
    print(my_func(n_weight, m_price, k1_price, k2_price))


if __name__ == '__main__':
    main()
