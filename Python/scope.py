def val(x):
    x=x+5
    return 'value of x in val: ', x

def kal(x):
    x=x+5
    return 'value of x in kal: ', x

def pal():
    global x    #don't pass args use global keyword
    x=x+5
    return 'value of x in pal: ', x

x=5
print('value of x: ', x)
print(val(x))
print(kal(x))
print(pal())
print('value of x: ', x)
