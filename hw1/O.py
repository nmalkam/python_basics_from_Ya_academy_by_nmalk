def o_clock(h, m, add):
    hours_in = 24
    minutes_in = 60

    def counter_full(num, divider):
        full_num = num // divider
        remainder = num - (full_num * divider)
        # if remainder < 10:
        #     remainder = "0" + str(remainder)
        return full_num, remainder

    m = m + add
    if m >= minutes_in:
        full_num, remainder = counter_full(m, minutes_in)
        # counter_full(m, 60)
        h += full_num
        m = remainder
    else:
        m = m
    if h >= hours_in:
        full_num, remainder = counter_full(h, hours_in)
        # counter_full(h, 24)
        h = remainder
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    print(f'{h}:{m}')


# assert o_clock(8, 0, 65) == "09:05"
# assert o_clock(10, 15, 2752) == "08:07"
# assert o_clock(0, 0, 1441) == "00:01"


def main():
    h = int(input())
    m = int(input())
    add = int(input())
    o_clock(h, m, add)


if __name__ == '__main__':
    main()
