"""Implement merge sort."""
import time
from random import randint

def merge_sort(alist):
    """Merge sort function."""
    if not alist:
        return

    if len(alist) > 1:
        midpoint = len(alist) // 2

        listA = alist[:midpoint]
        listB = alist[midpoint:]

        merge_sort(listA)
        merge_sort(listB)

        i = 0
        j = 0
        k = 0

        while i < len(listA) and j < len(listB):
            if isinstance(listA[i], str) or isinstance(listB[j], str):
                raise TypeError("Inputs cannot be strings.")

            if listA[i] < listB[j]:
                alist[k] = listA[i]
                i += 1
            else:
                alist[k] = listB[j]
                j += 1
            k += 1

        while i < len(listA):
            alist[k] = listA[i]
            i += 1
            k += 1

        while j < len(listB):
            alist[k] = listB[j]
            j += 1
            k += 1


def time_it(input_list):
    """Return avergae time of insertion sort run."""
    for i in range(501):
        start = time.time()
        merge_sort(input_list)
        time_passed = time.time() - start
    avg_time = time_passed / 500
    return avg_time

if __name__ == '__main__':
    small_list = time_it([2, 1])
    large_list = time_it([randint(0, 1000000) for i in range(10000)])
    print("Using divide and conquer, merge_sort splits a list into two sublists and makes recursive calls on"
        "those sublists, then compares the two lists to sort the values. Then puts the sorted sublists back into"
        "the original list")
    print("Input: [2, 1]\n\tnumber of runs: 500\n\taverage time: {}".format(small_list))
    print("Input: [randint(0, 1000000) for i in range(10000)]\n\tnumber of runs: 500\n\taverage time: {}".format(large_list))
