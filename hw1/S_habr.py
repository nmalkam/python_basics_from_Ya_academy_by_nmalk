def my_func(name, price_per_kg, weight, cash):
    print("================Чек================")
    cost = weight * price_per_kg
    returned = cash - cost
    to_print = [f"Товар:%s{name}", f"Цена:%s{weight}кг * {price_per_kg}руб/кг",
                f"Итого:%s{cost}руб", f"Внесено:%s{cash}руб", f"Сдача:%s{returned}руб"]
    for item in to_print:
        if len(str(item)) < 35:
            num_spaces = 35 - (len(str(item)) - 2)
            spaces = num_spaces * " "
            print(item % spaces)
    print("===================================")


def main():
    name = input()
    price_per_kg = int(input())
    weight = int(input())
    cash = int(input())
    my_func(name, price_per_kg, weight, cash)


if __name__ == '__main__':
    main()
