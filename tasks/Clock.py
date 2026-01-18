time = input()
h, m = map(lambda t: int(t), time.split(" "))
H = (12 - h) % 12
M = (60 - m) % 60
print(H, M)
