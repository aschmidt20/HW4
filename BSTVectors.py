import time
import random
import matplotlib.pyplot as plt
import bisect
import BalancingBinaryTree as bbt


"""
We consider a python list to be an equivalent to C++ vector
Now to do some timings 
"""

n_vals = [2 ** i for i in range(17)]
bst_insert_elapsed = []  # the time it took for the binary tree to handle insertion of n elements
vector_insert_elapsed = []  # the time it took for the list to handle insertion of n elements
iters = 10  # the number of times to repeat our experiment

for n in n_vals:
    vector = []
    bst = bbt.BinaryTree()
    random_keys = [random.randint(-100, 100) for i in range(n)]
    random_vals = [random.randint(-100, 100) for i in range(n)]

    # Time vector insertion
    start = time.clock()
    for a in range(iters):
        for i in range(n):
            bisect.insort(vector, (random_keys[i], random_vals[i]))  # Just for consistency, we insert a pair
    end = time.clock()
    # Append the true time per trial
    vector_insert_elapsed.append((end - start) / iters)

    # Time bst insertion
    start = time.clock()
    for a in range(iters):
        for i in range(n):
            bst.insert(random_keys[i], random_vals[i])
    end = time.clock()
    # Append the true time per trial
    bst_insert_elapsed.append((end - start) / iters)

plt.style.use('dark_background')
plt.plot(n_vals, vector_insert_elapsed, label = 'Vector')
plt.plot(n_vals, bst_insert_elapsed, label = 'Balanced Binary Tree')
plt.title("Vector Insertion vs Balanced Binary Tree Insertion ")
plt.legend()
plt.show()
