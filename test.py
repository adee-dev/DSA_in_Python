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
            if l[j] < l[minpos]:
                l[j], l[minpos] = l[minpos], l[j]
    return l


def insertion_sort(l):
    n = len(l)
    if n==0:
        return l
    for i in range(n):
        j=i
        while j>0 and l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
            j-=1
    return l

def merge(A,B):
    m,n=len(A),len(B)
    C,i,j,k=[],0,0,0
    while(k<m+n):
        if i==m:
            C.extend(B[j:])
            k+=n-j
        elif j==n:
            C.extend(A[i:])
            k+=m-i
        elif A[i]<B[j]:
            C.append(A[i])
            i,k=i+1,k+1
        else:
            C.append(B[j])
            j,k=j+1,k+1
    return C

def merge_sort(l):
    n=len(l)
    if n<=1:
        return l
    L,R=merge_sort(l[:n//2]),merge_sort(l[n//2:])
    ll=merge(L,R)
    return ll

def quick_sort(l):
    n=len(l)
    if n<=1:
        return l
    pivot=l[0]
    L=[x for x in l[1:] if x<pivot]
    R=[x for x in l[1:] if x>=pivot]
    return quick_sort(L)+[pivot]+quick_sort(R)

# l=list(range(10))
l = [6, 2, 1, 7, 4, 9, 3, 0, 8, 5]
k = 7
# print(selection_sort(l))
# print(insertion_sort(l))
# print(merge_sort(l))
print(quick_sort(l))
# print(binary_search(l, k))
