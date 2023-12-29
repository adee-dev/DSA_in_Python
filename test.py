def binary_search(l, k):
    n = len(l)
    if n == 0:
        return False
    mid = n // 2
    if l[mid] == k:
        return True
    elif l[mid] < k:
        return binary_search(l[mid + 1 :], k)
    else:
        return binary_search(l[:mid], k)


def selection_sort(l):
    n = len(l)
    if n == 0:
        return l
    for i in range(n):
        minpos = i
        for j in range(i + 1, n):
            if l[minpos] > l[j]:
                l[minpos], l[j] = l[j], l[minpos]
    return l


def insertion_sort(l):
    n = len(l)
    if n == 0:
        return l
    for i in range(n):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
    return l


def merge(A, B):
    m, n = len(A), len(B)
    C, i, j, k = [], 0, 0, 0
    while k < m + n:
        if j == n:
            C.extend(A[i:])
            k += m - i
        elif i == m:
            C.extend(B[j:])
            k += n - j
        elif A[i] < B[j]:
            C.append(A[i])
            k, i = k + 1, i + 1
        else:
            C.append(B[j])
            k, j = k + 1, j + 1
    return C


def merge_sort(l):
    n = len(l)
    if n <= 1:
        return l
    L = merge_sort(l[: n // 2])
    R = merge_sort(l[n // 2 :])

    C = merge(L, R)
    return C


def quick_sort(l):
    n = len(l)
    if n <= 1:
        return l
    pivot = l[0]
    L = [x for x in l[1:] if x < pivot]
    R = [x for x in l[1:] if x >= pivot]
    return quick_sort(L) + [pivot] + quick_sort(R)


# l = list(range(10))
l = [4, 7, 1, 0, 2, 8, 3, 9, 5, 6]
print(l)
# k = 7
# print(binary_search(l, k))
# print(selection_sort(l))
# print(insertion_sort(l))
# print(merge_sort(l))
print(quick_sort(l))
