__author__ = 'navneet'

count=0


def digits(n):
    ds = []
    while n > 0:
        ds.append(n % 10)
        n = n/10
    return ds

for num in range(1,1001):
    for val in digits(num):
        if val == 8:
            count = count+1

print count

def f(x):
    return (3-x)**2 + (1+x)**3


print 'low val is : '+str(f(2))


def recurFindInTree(tree, name):
    if tree == None:
        return None
    elif tree['name'] == name:
        return True
    else:
        return recurFindInTree(tree['right'],name) or recurFindInTree(tree['left'],name)