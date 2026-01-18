import time
import functools


def timer(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start = time.time_ns()
        value = func(*args, **kwargs)
        end = time.time_ns()
        run_time = end - start
        print(f'{func.__name__!r} time = {run_time} nc')
        return run_time

    return timer_wrapper


@timer
def quick_sorting(array):
    quick_sort(array, 0, len(array) - 1)


def quick_sort(array, start, end):
    def swap(arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def partition(arr, start, end):
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] <= pivot:
                i = i + 1
                swap(arr, i, j)
        swap(arr, i + 1, end)
        return i + 1

    if start < end:
        q = partition(array, start, end)
        quick_sort(array, start, q - 1)
        quick_sort(array, q + 1, end)


@timer
def insertion_sort(array):
    for i in range(1, len(array)):
        current_element = array[i]
        j = i - 1
        while j >= 0 and current_element < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = current_element


@timer
def selection_sort(array):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[j] < array[i]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
