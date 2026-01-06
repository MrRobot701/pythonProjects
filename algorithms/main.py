import math


def get_b():
    for r in range(0, 17):
        for q in range(0, 43):
            tmp = (9 * q + 25 * (17 - r))
            if tmp % 38 == 0:
                return tmp // 38


def get_b_other_way():
    a = 1
    while math.ceil(77 * a / 17) != math.floor(197 * a / 43):
        a += 1
    return math.ceil(77 * a / 17)


print(get_b())
print(get_b_other_way())
