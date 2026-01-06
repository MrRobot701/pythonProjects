def calculate(k1, m, k2, p2, n2):
    def div_ceil(a, b):
        return a // b + 1 if a % b > 0 else a // b

    if n2 > m:
        return -1, -1

    p1, n1 = -1, -1
    p1_solutions = set()
    n1_solutions = set()
    k2_floors = n2 + (p2 - 1) * m
    if k2_floors > 1:
        lower_bound = div_ceil(k2, k2_floors)
        upper_bound = div_ceil(k2, k2_floors - 1)
        possible_apartments_on_one_floor = lower_bound
        while possible_apartments_on_one_floor < upper_bound:
            k1_floors = div_ceil(k1, possible_apartments_on_one_floor)
            if k1_floors % m == 0:
                n1 = m
                p1 = k1_floors // m
            else:
                p1 = div_ceil(k1_floors, m)
                n1 = k1_floors - (p1 - 1) * m
            p1_solutions.add(p1)
            n1_solutions.add(n1)
            possible_apartments_on_one_floor += 1
    else:
        if k1 <= k2:
            n1 = 1
            p1 = 1
        elif k1 <= k2*m:
            n1 = 0
            p1 = 1
        else:
            n1 = 0
            p1 = 0
        if m == 1:
            n1 = 1

    if len(p1_solutions) < 2 and len(n1_solutions) < 2:
        return p1, n1
    elif len(p1_solutions) == 1:
        return p1, 0
    elif len(n1_solutions) == 1:
        return 0, n1
    else:
        return 0, 0


params = list(map(lambda param: int(param), input().split(" ")))
p, n = calculate(*params)
print(p, n)
