def binary_search(l,k):
    if len(l)==0:
        return 0
    mid=len(l)//2
    if l[mid]==k:
        return 1
    elif l[mid]>k:
        return binary_search(l[:mid], k)
    else:
        return binary_search(l[mid+1:],k)

l=list(range(10))
k=7
print(binary_search(l,k))
