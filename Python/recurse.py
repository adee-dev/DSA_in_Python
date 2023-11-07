def mini(l):
    m=l[0]
    for i in l:
        if i<m:
            m=i
    return m

def Sort(l):
    if len(l)==1 or l==[]:
        return l
    m=mini(l)
    l.remove(m)
    return [m]+Sort(l)

l=[5,2,3,1,4]
print(Sort(l))