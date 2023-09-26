def my_func(name, price_per_kg, weight, cash):
    num_spaces = 0
    spaces = num_spaces * " "
    cost = weight * price_per_kg
    returned = cash - cost

    # lambda x: x*2

    to_print = ["Товар:{}",lambda: f"Цена:{}{weight}кг * {}руб/кг",lambda: f"Итого:{}{cost}руб",lambda: f"Внесено:{}{cash}руб",lambda: f"Сдача:{}{returned}руб"]
    for item in to_print:
        if len(str(item)) < 35:
            num_spaces = 35 - len(str(item))
            spaces = num_spaces * " "
            print(item())
    print("===================================")

# some_list = [lambda: f"blabla {variable} uhti!"]
# for item in some_list :
# ..variable = "something new!"
# ..print(item())

assert my_func("черешня", 2, 3, 10) == ["================Чек================", "Товар:                      черешня", "Цена:                 3кг * 2руб/кг", "Итого:                         6руб", "Внесено:                      10руб", "Сдача:                         4руб", "==================================="]
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
