def load_tests():
    test = dict()
    path = "C:\\Users\\andre\\PycharmProjects\\algorithms\\yandex_and_young\\test_data\\G\\"
    for i in range(1, 24):
        number = "0" + str(i) if i < 10 else str(i)
        input = open(path + "Input" + number + ".txt", "r")
        output = open(path + "Answer" + number + ".txt", "r")
        test[input.readline().split("\n")[0]] = output.readline().split("\n")[0]
        input.close()
        output.close()
    return test


def do_test(test, func):
    i = 1
    for input in test:
        params = list(map(lambda d: int(d), input.split(" ")))
        p, n = func(*params)
        result = str(p) + " " + str(n)
        if result == test[input]:
            print(f'{i}) pass')
        else:
            print(f'{i}) fail on {input}: right = {test[input]}, yours = {result}')
        i += 1