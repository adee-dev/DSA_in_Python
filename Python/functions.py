def mini(l):
    l.sort()
    return l[0]

def maxi(l):
    l.sort()
    return l[len(l)-1]

def avgearge(l):
    sum=0
    for i in l:
        sum+=i
    return sum/len(l)

def append_back(l, m):
    for i in m:
        l.append(i)
    return l

def append_front(l,m):
    for i in l:
        m.append(i)
    return m

l=[1,4,6,2,9,8,3]
m=[10,2,7,4,69,99,-1,1]

print(mini(l))
print(maxi(m))
print(avgearge(l))
print(append_back(l,m))
print(append_front(l,m))