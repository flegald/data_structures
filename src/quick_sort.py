"""Quick sort method."""
import time
from random import randint


def quick_sort(alist):
    """Implement a quick sort on a list."""
    low = []
    high = []
    # import pdb; pdb.set_trace()
    try:
        pivot = alist[0]
        for i in alist[1:]:
            if isinstance(i, str):
                raise TypeError("List can not contain string.")
            high.append(i) if i > pivot else low.append(i)
        return quick_sort(low) + [pivot] + quick_sort(high)
    except IndexError:
        return []


def time_it(input_list):
    """Return avergae time of quick sort run."""
    for i in range(501):
        start = time.time()
        quick_sort(input_list)
        time_passed = time.time() - start
    avg_time = time_passed / 500
    return avg_time

if __name__ == '__main__':
    small_list = time_it([2, 1])
    large_list = time_it([randint(0, 1000000) for i in range(10000)])
    print("Starting at the 1sth index of a list, quick sort compares "
            "the value at the current index with all of the previous spots in the list "
            "until the list is sorted.")
    print("Input: [2, 1]\n\tnumber of runs: 500\n\taverage time: {}".format(small_list))
    print("Input: [randint(0, 1000000) for i in range(10000)]\n\tnumber of runs: 500\n\taverage time: {}".format(large_list))
