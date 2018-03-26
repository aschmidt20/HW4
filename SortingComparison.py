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
points = [1,10,100,1000]
for i in points:
    random_array = []
    random_array_copy = list(random_array)
    start = time.clock()
    for a in range(50):
        for b in range(0, i):
            random_array.append(random.randint(-100, 100))
        insertionSort(random_array)
    end = time.clock()
    time_insertion_sort = (end - start) / 50
    start = time.clock()
    for c in range(50):
        for d in range(0, i):
            random_array.append(random.randint(-100, 100))
        quickSort(random_array)
    end = time.clock()
    time_quick_sort = (end - start) / 50
    insertion_sort_times.append(time_insertion_sort)
    quick_sort_times.append(time_quick_sort)

plt.style.use('dark_background')
plt.plot(points, insertion_sort_times, label='Insertion Sort')
plt.plot(points, quick_sort_times, label='Quick Sort')
plt.title("Effect Of Input Size On Insertion and Quick Sort Runtime")
plt.xlabel("Input Size")
plt.ylabel("Average Run Time (ms)")
plt.legend()
plt.show()