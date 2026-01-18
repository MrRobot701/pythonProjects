import functools

from collection.heap.MaxHeap import heapSort

def new_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapping function")
        result = func(*args, **kwargs)
        print("Wrapped")
        return result
    return wrapper


@new_func
def f(*args):
    for a in args: print(a)

arr = [1, 2, -1, 0, 10, -3, 4, 3, 6, 7]
print(arr)
heapSort(arr, len(arr))
print(arr)

var = 1
print((1).is_integer())
answer = True
if isinstance(answer, int):
    print("What's the question?")
    print(type(answer))


class Test:
    var = "boo"

    def __init__(self, message = None):
        if message is not None: self.var = message

    def test(self, message = None):
        if message is not None: self.var = message
        return self.var

    def __str__(self):
        return str(self.var)


t = Test()
print(t.test())

t = (Test(1), Test(2))
print(t[0], t[1])
t[0].test(3)
print(t[0], t[1])

f(1, 2, 3, 4, 5)