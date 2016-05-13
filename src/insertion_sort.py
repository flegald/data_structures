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
    for i in range(1, len(alist)):
        val = alist[i]
        left_index = i - 1
        while left_index >= 0 and alist[left_index] > val:
            alist[left_index + 1] = alist[left_index]
            left_index -= 1
        alist[left_index + 1] = val
    return alist


def insertion_sort_stability_proof(list_of_tuples):
    """Implementing the same sort but with tuples to show stability."""
    if not list_of_tuples:
        return
    for i in range(1, len(list_of_tuples)):
        if isinstance(list_of_tuples[i], str):
            raise TypeError("List cannot include strings")
    for i in range(1, len(list_of_tuples)):
        val = list_of_tuples[i]
        left_index = i - 1
        while left_index >= 0 and list_of_tuples[left_index][1] > val[1]:
            list_of_tuples[left_index + 1] = list_of_tuples[left_index]
            left_index -= 1
        list_of_tuples[left_index + 1] = val
    return list_of_tuples


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
