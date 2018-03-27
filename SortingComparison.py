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

quick_sort_times = []
insertion_sort_times = []
points = arange(1, 50, 5)
iters = 1000
for point in points:

    # Time insertion sort
    start = time.clock()
    for a in range(iters):
        # We note the noise added by timing the creation of this array, but also argue that it is minimal
        # and balanced since it is done in both trials.
        random_array = [random.randint(-100, 100) for i in range(point)]
        insertionSort(random_array)
    end = time.clock()
    time_insertion_sort = (end - start) / iters

    # Time quick sort
    start = time.clock()
    for c in range(iters):
        random_array = [random.randint(-100, 100) for i in range(point)]
        quickSort(random_array)
    end = time.clock()
    time_quick_sort = (end - start) / iters

    insertion_sort_times.append(time_insertion_sort)
    quick_sort_times.append(time_quick_sort)

plt.style.use('dark_background')
plt.plot(points, insertion_sort_times, label='Insertion Sort')
plt.plot(points, quick_sort_times, label='Quick Sort')
# plt.plot(points, [insertion_sort_times[i] - quick_sort_times[i] for i in range(len(points))])
plt.title("Effect Of Input Size On Insertion and Quick Sort Runtime")
plt.xlabel("Input Size")
plt.ylabel("Average Run Time (ms)")
plt.legend()
plt.show()
