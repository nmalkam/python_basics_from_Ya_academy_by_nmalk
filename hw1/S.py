def my_func(name, price_per_kg, weight, cash):
    # def counter_raw(to_print, spaces):
    #     # print("def")
    #     return to_print[index]
    # new_to_print = ["1", "2", "3", "4", "5"]
    # index = 0
    # num_spaces = 0
    # spaces = num_spaces * " "
    cost = weight * price_per_kg
    returned = cash - cost
    print("================Чек================")
    print(f"Товар:{(35-6-len(str(name)))*' '}{name}")
    print(f"Цена:{(35-16-len(str(weight)) -len(str(price_per_kg)))*' '}{weight}кг * {price_per_kg}руб/кг")
    print(f"Итого:{(35-9-len(str(cost)))*' '}{cost}руб")
    print(f"Внесено:{(35-11-len(str(cash)))*' '}{cash}руб")
    print(f"Сдача:{(35-9-len(str(returned)))*' '}{returned}руб")
    print("===================================")

    # to_print = [f"Товар:{spaces}{name}", f"Цена:{spaces}{weight}кг * {price_per_kg}руб/кг", f"Итого:{spaces}{cost}руб", f"Внесено:{spaces}{cash}руб", f"Сдача:{spaces}{returned}руб"]
    # for _ in to_print:
    #     if len(str(_) <) 35:
    #         num_spaces = 35 - len(str(_)
    #         spaces = num_spaces * " "
    #         # counter_raw(to_print, spaces)
    #         print(counter_raw(to_print, spaces))
    #         index += 1
    # print("===================================")


# assert my_func("черешня", 2, 3, 10) == ["================Чек================", "Товар:                      черешня", "Цена:                 3кг * 2руб/кг", "Итого:                         6руб", "Внесено:                      10руб", "Сдача:                         4руб", "==================================="]
# assert my_func("манго", 187, 43, 8041) == ["================Чек================, Товар:                        манго, Цена:              43кг * 187руб/кг, Итого:                      8041руб, Внесено:                    8041руб, Сдача:                         0руб, ==================================="]

# assert phone('8(495)430-23-97', ['+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', '8-495-430']) == ['YES', 'YES', 'NO']


def main():
    name = input()
    price_per_kg = int(input())
    weight = int(input())
    cash = int(input())
    print([my_func(name, price_per_kg, weight, cash)])


if __name__ == '__main__':
    main()

# ================Чек================
# Товар:                    <продукт>
# Цена:     <число>кг * <число>руб/кг
# Итого:                   <число>руб
# Внесено:                 <число>руб
# Сдача:                   <число>руб
# ===================================
