
# strings
s = "abcdefghijklmnopqrstuvwxyz"
print(s[8])
print(len(s))
print(s[-1], s[1])
print(s[0] + s[25])

# chanining suckers

a = 2
print(1 < a < 3)
print(1 < a > 3)
print(1 == a > 3)
print(1 == a == 3)
print(1 == a != 3)
print(a < 10 > a * 2 < 100)

def hi():
    print(hi)

x='''
hii gg
'''
y="hi ggg"

print(x.capitalize())
print(y.capitalize())

x='AdItyA'
y='----he---he----'

print(x.lower())
print(x.upper())
print(x.title())
print(x.capitalize())
print(x.swapcase())
print(x.swapcase())
print(x.islower())
print(x.isalpha())
print(x.isalnum())
print(x.isascii())
print(x.isdigit())

print(y.strip('-'))
print(y.lstrip('-'))
print(y.rstrip('-'))

print(x.startswith('A'))
print(x.startswith('z'))

print(x.count('A'))
print(x.index('y'))
print(x.replace('A','a'))