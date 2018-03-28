import time
import random
import matplotlib.pyplot as plt
import BalancingBinaryTree as bbt  # our binary tree implementation
from numpy import linspace

"""
We consider a python dictionary to be an efficient realization of the hash table data structure. 
Now to do some timings 
"""

n_vals = [2 ** n for n in range(19)]
bst_insert_elapsed = []  # the time it took for the binary tree to handle insertion of n elements
ht_insert_elapsed = []  # the time it took for the hash table to handle insertion of n elements
iters = 5  # the number of times to repeat our experiment

for n in n_vals:
    hash_tab = {}
    bst = bbt.BinaryTree()
    random_keys = [random.randint(-100, 100) for i in range(n)]
    random_vals = [random.randint(-100, 100) for i in range(n)]

    # Hash Table Testing
    start = time.clock()
    # Repeat the experiment however many times
    for a in range(iters):
        for i in range(n):
            hash_tab[random_keys[i]] = random_vals[i]
    end = time.clock()
    # Append the true time per trial
    ht_insert_elapsed.append((end - start)/iters)

    # BST Insertion Testing
    start = time.clock()
    for a in range(iters):
        for i in range(n):
            bst.insert(random_keys[i], random_vals[i])
    end = time.clock()
    bst_insert_elapsed.append((end - start)/iters)

plt.style.use('dark_background')
plt.plot(n_vals, ht_insert_elapsed, label = 'Hash Table')
plt.plot(n_vals, bst_insert_elapsed, label = 'Bineary tree')
plt.legend()
plt.title("Hash Table vs Balanced Binary Tree Insertion")
plt.show()