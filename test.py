"""
binary search
"""


def binary_search(l, k):
    if l == []:
        return False
    mid = len(l) // 2
    if l[mid] == k:
        return True
    elif l[mid] < k:
        return binary_search(l[mid + 1 :], k)
    else:
        return binary_search(l[:mid], k)


"""
selection sort
"""


def selection_sort(l):
    # 5 1 3 2 4
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        min_position = i
        for j in range(i + 1, n):
            if l[j] < l[min_position]:
                min_position = j
        l[min_position], l[i] = l[i], l[min_position]
    return l


"""
insertion sort
"""


def insertion_sort(l):
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        j = i
        while l[j] < l[j - 1] and j > 0:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
    return l


# l = list(range(10))
l = [5, 1, 3, 2, 4]
# print(selection_sort(l))
print(insertion_sort(l))
# k = 99
# print(binary_search(l, k))
