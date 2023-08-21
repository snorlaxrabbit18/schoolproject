# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import math
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


import random
N = int(input("Enter positive N: "))
randomlist = random.sample(range(1, 30), N)
print(randomlist)

pancake = randomlist
k = N
while(k>1):
    print(pancake)
    curr_list = pancake[0:k]
    max_val = max(curr_list);
    max_idx = curr_list.index(max(curr_list))
    if(max_idx == k-1):
        k = k-1
    elif(max_idx == 0):
        curr_list = curr_list[-1::-1]
        pancake[0:k] = curr_list
        print(pancake)
        k = k-1
    else:
        curr_list[0:max_idx+1] = curr_list[max_idx::-1]
        curr_list = curr_list[-1::-1]
        pancake[0:k] = curr_list
        print(pancake)
        k = k-1
print(pancake)