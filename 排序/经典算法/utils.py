# coding=utf-8
from random import randint
import timeit


def generateRandomArray(n, min, max):
    arr = []
    arr = [randint(min, max) for x in range(n)]
    return arr


def generateNearlyOrderedArray(n, swapTimes):
    arr = []
    for i in range(n):
        arr.append(i)
    for j in range(swapTimes):
        posx = randint(0, n - 1)
        posy = randint(0, n - 1)
        arr[posx], arr[posy] = arr[posy], arr[posx]
    return arr


def isSorted(alist):
    for i in range(0, len(alist) - 1):
        if alist[i] > alist[i + 1]:
            return False
    return True


# t1 = timeit.Timer('testSort("某种排序算法函数", alist)', 'from __main__ import testSort, 某种排序算法函数, alist')
# print('某种排序算法：%s s' % t1.timeit(number=1))


# func表示要检测的算法函数，alist为传入的数列
def testSort(func, alist):
    alist = func(alist)
    assert isSorted(alist), "排序算法错误\n"
