def selection_sort(l):
    # 3 1 4 5 2
    n=len(l)
    if n==0:
        return l
    for i in range(n):
        min_pos=i
        for j in range(i+1, n):
            if l[j]>l[min_pos]:
                min_pos=j
        l[i], l[min_pos]=l[min_pos],l[i]
    return l

def insertion_sort(l):
    n=len(l)
    if n==0:
        return l
    for i in range(n):
        j=i
        while(j>0 and l[j]<l[j-1]):
            l[j],l[j-1]=l[j-1],l[j]
            j-=1
    return l

l=[2,1,5,4,3]
print(selection_sort(l))
print(insertion_sort(l))