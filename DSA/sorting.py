def selection_sort(l):
    n = len(l)
    if n == 0:
        return l
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if l[j] > l[min_pos]:
                l[min_pos], l[j] = l[j], l[min_pos]
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
            k += n - i
        elif A[i] < B[j]:
            C.append(A[i])
            i, k = i + 1, k + 1
        else:
            C.append(B[j])
            j, k = j + 1, k + 1
    return C


def merge_sort(l):
    n = len(l)
    if n <= 1:
        return l
    L = merge_sort(l[: n // 2])
    R = merge_sort(l[n // 2 :])
    B = merge(L, R)
    return B


def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        left = [x for x in l[1:] if x < pivot]
        right = [x for x in l[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


l = [3, 1, 5, 4, 2]
# print(selection_sort(l))
# print(insertion_sort(l))
# print(merge_sort(l))
print(quick_sort(l))
