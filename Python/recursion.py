"""
calculates sum till n
"""


# * verified
def sum(n):
    if n == 1:
        return n
    return n + sum(n - 1)

# * verified
def compound_intrest(p, n): #intrest is 10%
    if n==1:
        return n*1.1
    return (compound_intrest(p, n-1)*1.1)

#* verified
def factorial(n):
    if n==1 or n==0:
        return n
    return factorial(n-1)*n