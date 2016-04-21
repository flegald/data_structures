"""Insertion Sort."""
import time
from random import randint


def insertion_sort(alist):
    """Return sorted list using insertion sort algorithm."""
    if not alist:
        return
    for i in range(1, len(alist)):
        if isinstance(alist[i], str):
            raise TypeError("List cannot include strings")
        current_value = alist[i]
        index = i

        while index > 0 and alist[index - 1] > current_value:
            alist[index] = alist[index - 1]
            index = index - 1
        alist[index] = current_value


def time_it(input_list):
    """Return avergae time of insertion sort run."""
    for i in range(501):
        start = time.time()
        insertion_sort(input_list)
        time_passed = time.time() - start
    avg_time = time_passed / 500
    return avg_time

if __name__ == '__main__':
    small_list = time_it([2, 1])
    large_list = time_it([randint(0, 1000000) for i in range(10000)])
    print("Starting at the 1sth index of a list, insertion sort compares "
            "the value at the current index with all of the previous spots in the list "
            "until the list is sorted.")
    print("Input: [2, 1]\n\tnumber of runs: 500\n\taverage time: {}".format(small_list))
    print("Input: [randint(0, 1000000) for i in range(10000)]\n\tnumber of runs: 500\n\taverage time: {}".format(large_list))
