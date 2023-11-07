"""

l=[i for i in range(10)]
s={i for i in range(10)}

print(l, s, sep="\n")


# we can't perform s[i] operation on set
# we can use in and its damn fast
#list       set
# x         search/belonging
#l[0]       x

s.add(10)
print(s)

s='iuhsadisauhiusahiusahiasdhiuasdhiuasdhisadhudasiudsaidasdsadsaidsauih'

l=[_ for _ in s]
print(l)
s=set(l)
print(s)
d={}
for _ in l:
    d[_]=0
for _ in l:
    d[_]+=1
print(d)
# l=list(range(10))
# t=tuple(range(10))
# # t=(1,2,3,4,5)
# print(t)
# print(l)

l=list(range(10))
# print(l)
# list is passed as reference to the function
m=l.copy()
l.append(10)
l.remove(10)
l.insert(0,10)
l.pop()
l.sort()
l.reverse()
print(l)
print(m)

t = (1, 2, 3)
print(t, type(t))

x, y, z = t
print(x, y, z)

i = 10  # IT'S AN INTEGER!!!
j = (10,)  # Its a TUPLE
l = ([1, 2, 3], [4, 5])  # we cant change lists but can modify vals in list

#if tuple have all mutable elements its hashable and if dont its not hashable
# we can use tuples as keys in dict if its hashable and otherwise not
k=list(range(10))
v=list(range(10,20))

d={}
for i in k:
    d[k[i]]=v[i]
print(d)

k=[k for k in d.keys()]
v=[v for v in d.values()]
items=[item for item in d.items()]
print(k, v, items)

print(d.keys())
print(d.values())
print(d.items())
"""
A={1,2,3,4,5}
B={6,7,8,9,0}

print(A.issubset(B))
print(A | B)
print(A.union(B))
print(A.intersection(B), A & B)
print(A-B)
print(A.difference(B))


