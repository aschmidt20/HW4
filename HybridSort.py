import random
import time
from numpy import *
import numpy as np
import matplotlib.pyplot as plt



# Function to do insertion sort
# Source: https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Source: rosettacode.org
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


# Source: rosettacode.org
def hybridSort(arr, cutoff):
    less = []
    pivotList = []
    more = []
    if len(arr) <= cutoff:
        return insertionSort(arr)
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

points = [1,10, 50, 100, 200, 400, 700, 1000]
cutoffs = [5, 10, 20, 30, 50, 100, 200]
quick_sort_times = []
insertion_sort_times = []
hybrid_sort_times = dict((cutoff, []) for cutoff in cutoffs)
iters = 50
for point in points:

    # Time insertion sort on the inputs
    start = time.clock()
    for a in range(iters):
        random_array = [random.randint(-100, 100) for i in range(point)]
        insertionSort(random_array)
    end = time.clock()
    time_insertion_sort = (end - start) / iters

    # Time quick sort on the inputs
    start = time.clock()
    for c in range(iters):
        random_array = [random.randint(-100, 100) for i in range(point)]
        quickSort(random_array)
    end = time.clock()
    time_quick_sort = (end - start) / iters

    for cutoff in cutoffs:
        start = time.clock()
        for e in range(iters):
            random_array = [random.randint(-100, 100) for i in range(point)]
            hybridSort(random_array, cutoff)
        end = time.clock()
        hybrid_sort_times[cutoff].append((end - start) / iters)

    insertion_sort_times.append(time_insertion_sort)
    quick_sort_times.append(time_quick_sort)

plt.style.use('dark_background')
# plt.plot(points, insertion_sort_times, label='Insertion Sort')
plt.plot(points, quick_sort_times, label='Quick Sort')
for cutoff in cutoffs:
    if all([quick_sort_times[i] - hybrid_sort_times[cutoff][i] for i in range(len(points))]) > 0:
        plt.plot(points, hybrid_sort_times[cutoff], label = 'Hybrid Cutoff = ' + str(cutoff), ls = '--')
plt.title("Insertion Sort, Merge Sort, Hybrid Performances")
plt.xlabel("Input Size")
plt.ylabel("Average Run Time (ms)")
plt.legend()
plt.show()