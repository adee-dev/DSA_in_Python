def binary_search(l, k):
    if l == []:
        return 0
    mid = len(l) // 2
    if l[mid] == k:
        return 1
    elif l[mid] > k:
        return binary_search(l[:mid], k)
    else:
        return binary_search(l[mid + 1 :], k)


l = list(range(10))
k = 99
print(binary_search(l, k))
