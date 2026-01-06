def my_min(*params):
    m = params[0]
    for i in range(1, len(params)):
        if m > params[i]:
            m = params[i]
    return m


def my_max(*params):
    M = params[0]
    for i in range(1, len(params)):
        if M < params[i]:
            M = params[i]
    return M


def calculate_table_area(a1, b1, a2, b2):
    A = my_min(a1, b1) + my_min(a2, b2)
    B = my_max(a1, b1, a2, b2)
    return A, B


sizes = list(map(lambda size: int(size), input().split(" ")))
a, b = calculate_table_area(*sizes)
print(a, b)
