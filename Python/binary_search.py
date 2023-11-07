import time

def simple_search(l,k):
    if k in l:
        return 1
    return 0

def binary_search(l,k):
    begin=0
    end=len(l)-1
    while(end>=begin):
        mid=(end+begin)//2
        if l[mid]==k:
            return 1
        if l[mid]>k:
            end=mid-1
        else:
            begin=mid+1
    
    return 0

def recursive_binary(l,k):
    if l==[]:
        return 0
    
    mid=len(l)//2
    
    if l[mid]==k:
        return 1
    elif l[mid]>k:
        return recursive_binary(l[:mid], k)
    else:
        return recursive_binary(l[mid+1:], k)

l=list(range(1000))
k=999
# print('----------------------------------')
# a=time.time()
# print(simple_search(l, k))
# b=time.time()
# print(b-a)
# print('----------------------------------')
# a=time.time()
# print(binary_search(l, k))
# b=time.time()
# print(b-a)
# print('----------------------------------')
print(recursive_binary(l, k))