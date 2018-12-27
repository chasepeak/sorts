import random

def selection_sort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]


def insertion_sort(alist):
    for i in range(len(alist) - 1):
        j = i + 1
        while j > 0:
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            elif alist[j] >= alist[j - 1]:
                j = 0
            j -= 1


def merge_sort(alist):
    if len(alist) > 20:
        mid = len(alist) // 2
        left_half = alist[:mid]
        merge_sort(left_half)
        right_half = alist[mid:]
        merge_sort(right_half)
        merge(alist, left_half, right_half)
    else:
        insertion_sort(alist)

def merge(alist, left_half, right_half):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            alist[k] = left_half[i]
            i += 1
        else:
            alist[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        alist[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        alist[k] = right_half[j]
        j += 1
        k += 1
    return alist


def quick_sort(alist):
    rec_quick_sort(alist, 0, len(alist) - 1)

def rec_quick_sort(alist, left, right):
    if right - left > 20:
        split_pt = partition(alist, left, right)
        rec_quick_sort(alist, left, split_pt - 1)
        rec_quick_sort(alist, split_pt + 1, right)
    else:
        insertion_sort(alist)

def partition(alist, left, right):
    pivot_val = median_of_three(alist, left, right)
    i = left
    j = right - 1
    done = False
    while not done:
        i += 1
        j -= 1
        while alist[i] < pivot_val:
            i += 1
        while alist[j] > pivot_val:
            j -= 1
        if i < j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            done = True
    alist[right - 1], alist[i] = alist[i], alist[right - 1]
    return i

def median_of_three(alist, left, right):
    center = (left + right) // 2
    if alist[center] < alist[left]:
        alist[left], alist[center] = alist[center], alist[left]
    if alist[right] < alist[left]:
        alist[right], alist[left] = alist[left], alist[right]
    if alist[right] < alist[center]:
        alist[center], alist[right] = alist[right], alist[center]

    alist[center], alist[right - 1] = alist[right - 1], alist[center] #this places the pivot at index (right - 1)
    return alist[right - 1]


def scramble(alist):
    for i in range(len(alist)):
        x = random.randrange(len(alist))
        alist[i], alist[x] = alist[x], alist[i]


def heap_sort(alist):
   pass #import heap
