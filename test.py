def binary_search(l, k):
    if len(l) == 0:
        return False
    mid = len(l) // 2
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
        if i == m:
            C.extend(B[j:])
            k += n - j
        elif j == n:
            C.extend(A[i:])
            k += m - i
        elif A[i] < B[j]:
            C.append(A[i])
            k, i = k + 1, i + 1
        else:
            C.append(B[j])
            j, k = j + 1, k + 1
    return C


def merge_sort(l):
    n = len(l)
    if n <= 1:
        return l
    L = merge_sort(l[n // 2 :])
    R = merge_sort(l[: n // 2])
    ll = merge(L, R)
    return ll


def quick_sort(l):
    if len(l)<=1:
        return l
    else:
        pivot=l[0]
        left=[x for x in l[1:] if x<pivot]
        right=[x for x in l[1:] if x>=pivot]
        return quick_sort(left)+[pivot]+quick_sort(right)


# l=list(range(10))
l = [2, 9, 6, 3, 7, 1, 8, 5, 4, 0]
k = 1
# print(selection_sort(l))
# print(insertion_sort(l))
# print(merge_sort(l))
print(quick_sort(l))
# print(binary_search(l,k))
