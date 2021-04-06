def bubble(l):
    if len(l) < 2:
        return l
    flag, first = 0, 1
    while first or flag:
        first, flag = 0, 0
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                # tmp = l[i]
                # l[i] = l[i + 1]
                # l[i + 1] = tmp
                # flag = 1
                l[i], l[i + 1] = l[i + 1], l[i]
                flag = 1
    return l


def bubbleSort2(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

l = [2, 3, 4, 1]
bubble(l)
print(l)
