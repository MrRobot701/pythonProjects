params = list(map(lambda param: int(param), input().split(" ")))
mode = input()


def operate(t_room, t_cond, mode):
    if mode == "freeze":
        return t_cond if t_room > t_cond else t_room
    elif mode == "heat":
        return t_cond if t_room < t_cond else t_room
    elif mode == "auto":
        return t_cond
    else:
        return t_room


print(operate(params[0], params[1], mode))
