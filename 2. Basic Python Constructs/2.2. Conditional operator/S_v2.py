x = float(input())
y = float(input())
c = (x ** 2 + y ** 2) ** 0.5  
y_para = (0.25 * (x ** 2)) + (0.5 * x) + 8.75
if x >= 0 and y >= 0: 
    if c <= 5: 
        print("Опасность! Покиньте зону как можно скорее!")
    elif c > 10:  
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x <= 0 and y >= 0:  
    if y <= 5 and y <= ((5 * x) + 35) / 3:
        print("Опасность! Покиньте зону как можно скорее!")
    elif c > 10: 
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif (x >= 0 and y <= 0) or (x <= 0 and y <= 0):  
    if y < y_para:
        print("Опасность! Покиньте зону как можно скорее!")
    elif c > 10:  
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x == 0 and y == 0:
    print("Опасность! Покиньте зону как можно скорее!")
