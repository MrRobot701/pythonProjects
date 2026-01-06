def find_solution(a, b, c):
    if c < 0:
        return "NO SOLUTION"
    elif a != 0:
        x = (c * c - b) / a
        return int(x) if x.is_integer() else "NO SOLUTION"
    elif b == c * c:
        return "MANY SOLUTIONS"
    else:
        return "NO SOLUTION"


a = int(input())
b = int(input())
c = int(input())
print(find_solution(a, b, c))
