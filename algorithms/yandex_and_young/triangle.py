def check_triangle(a, b, c):
    return "YES" if a + b > c and a + c > b and b + c > a else "NO"


a = int(input())
b = int(input())
c = int(input())

print(check_triangle(a, b, c))
