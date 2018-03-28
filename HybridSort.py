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

points = [1, 10, 30, 40, 50, 70, 80, 100, 200, 300, 400, 600, 800, 1000, 1500, 2000, 2500, 3000, 4000, 6000, 10000,
          20000, 30000]
cutoffs = [5, 15, 20, 27, 35, 50, 100, 1000]
quick_sort_times = []
insertion_sort_times = []
hybrid_sort_times = dict((cutoff, []) for cutoff in cutoffs)
iters = 30
for point in points:



    # Time quick sort on the inputs
    start = time.clock()
    for c in range(iters):
        random_array = [random.randint(-100, 100) for i in range(point)]
        quickSort(random_array)
    end = time.clock()
    time_quick_sort = (end - start) / iters

    # Time on every cutoff
    for cutoff in cutoffs:
        start = time.clock()
        for e in range(iters):
            random_array = [random.randint(-100, 100) for i in range(point)]
            hybridSort(random_array, cutoff)
        end = time.clock()
        hybrid_sort_times[cutoff].append((end - start) / iters)


    quick_sort_times.append(time_quick_sort)

# Time insertion sort separately, it takes too long on the large inputs
for point in points[0:5]:
# Time insertion sort on the inputs
    start = time.clock()
    for a in range(iters):
        random_array = [random.randint(-100, 100) for i in range(point)]
        insertionSort(random_array)
    end = time.clock()
    time_insertion_sort = (end - start) / iters
    insertion_sort_times.append(time_insertion_sort)

plt.style.use('dark_background')
f, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharex='col', sharey='row')
ax1.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[0]])
ax1.set_title("k = " + str(cutoffs[0]))
ax2.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[1]])
ax2.set_title("k = " + str(cutoffs[1]))
ax3.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[2]])
ax3.set_title("k = " + str(cutoffs[2]))
ax4.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[3]])
ax4.set_title("k = " + str(cutoffs[3]))
ax5.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[4]])
ax5.set_title("k = " + str(cutoffs[4]))
ax6.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[5]])
ax6.set_title("k = " + str(cutoffs[5]))
ax7.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[6]])
ax7.set_title("k = " + str(cutoffs[6]))
ax8.plot(points, quick_sort_times, points, hybrid_sort_times[cutoffs[7]])
ax8.set_title("k = " + str(cutoffs[7]))
f.suptitle("Hybrid Sort (yellow) vs Quicksort, Varying Cutoff")


plt.figure(2)
# plt.plot(points, insertion_sort_times, label='Insertion Sort')
plt.plot(points, quick_sort_times, label='Quick Sort')
plt.plot(points, hybrid_sort_times[27], label = 'Hybrid k = 27')
plt.title("Insertion Sort, QuickSort, Best Hybrid")
plt.xlabel("Input Size")
plt.ylabel("Average Run Time (ms)")
plt.legend()
plt.show()