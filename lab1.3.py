import sys
import random
import time


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                n = list[j + 1]
                list[j + 1] = list[j]
                list[j] = n


def gnome_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                n = list[j + 1]
                list[j + 1] = list[j]
                list[j] = n
                if j > 0:
                    j = j - 1


def block_sort(list):
    if (len(list) != 0):
        min = list[0]
        max = list[0]
        for item in list:
            if (item > max): max = item
            if (item < min): min = item
        n = int((max - min) / 5) + 1
        if n > 5:
            block1 = []
            block2 = []
            block3 = []
            block4 = []
            block5 = []
            for item in list:
                if (min + n > item):
                    block1.append(item)
                elif (min + 2 * n > item):
                    block2.append(item)
                elif (min + 3 * n > item):
                    block3.append(item)
                elif (min + 4 * n > item):
                    block4.append(item)
                else:
                    block5.append(item)
            block_sort(block1)
            block_sort(block2)
            block_sort(block3)
            block_sort(block4)
            block_sort(block5)
            i = 0
            for block in [block1, block2, block3, block4, block5]:
                for item in block:
                    list[i] = item
                    i += 1
            return list
        else:
            return bubble_sort(list)
    else:
        return list


def piramid_check_child(i, n, massiv):
    largest = 0
    left = 2 * i
    right = 2 * i + 1
    if left <= n:
        if massiv[left] > massiv[i]:
            largest = left
        else:
            largest = i
    else:
        largest = i

    if right <= n:
        if massiv[right] > massiv[largest]:
            largest = right
    if i != largest:
        temp = massiv[i]
        massiv[i] = massiv[largest]
        massiv[largest] = temp
        piramid_check_child(largest, n, massiv)


def piramid_build(massiv, n):
    for i in range(int(n / 2), 0, -1):
        piramid_check_child(i, n, massiv)


def piramid_sort(massiv):
    piramid_build(massiv, len(massiv) - 1)
    for i in range(len(massiv) - 1, 1, -1):
        massiving = massiv[1]
        massiv[1] = massiv[i]
        massiv[i] = massiving
        piramid_check_child(1, i - 1, massiv)


ListN = []
for i in range(30):
    ListN.append(random.randint(0, 10000))
piramid_sort(ListN)
print(ListN)
