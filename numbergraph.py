"""输入一个整数 k (k < 50), 输出一个 k*k 的九宫图。

示例：
5*5

17 24 01 08 15

23 05 07 14 16

04 06 13 20 22

10 12 19 21 03

11 18 25 02 09
"""


import random


def exch(arr, a, b):
    tamp = arr[a]
    arr[a] = arr[b]
    arr[b] = tamp


def shuffle(arr):
    """Rearrange array so that result is a uniformly random permutation.

    Args:
        arr: A list instance.
    """
    for i in range(len(arr)):
        r = random.randrange(i + 1)
        exch(arr, i, r)


# creat the asked array and shuffle it
x = int(input())
arr = list(range(1, x * x + 1))
shuffle(arr)

# print the number graph
width = len(str(x * x))
for i in range(x * x):
    if i % x == 0:
        print('\n')
    print('%0*d' % (width, arr[i]), end=" ")
