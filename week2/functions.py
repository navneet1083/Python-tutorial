def max(x,y):
    if x > y:
        return x
    else:
        return y

def iterativePower(x,p):
    result=1
    for turn in range(p):
        print('iteration: '+str(turn) + 'current result : '+str(result))
        result = result * x
    return result


def square(x):
    return x*x

def f(x):
    y = 1
    x = x+1
    print ('x is : '+str(x))
    return x

def twoPower(x,n):
    while n>1:
        x=square(x)
        n=n/2
    return x

def clip(lo,x,hi):
    if min(x,lo) == x:
        return lo
    elif max(x,hi) == x:
        return hi
    else:
        return x

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return max(lo,min(x,hi))

def f2(x):
    return x + 2
    def f3(x):
        return 2

def countNoVowels(s):
    vowelCount=0
    for c in s:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowelCount = vowelCount+1
    print('Number of vowels: '+str(vowelCount))

def countingBobs(s):
    count=0
    bobcount = 0
    for c in s:
        expectedStr = s[count:count+3]
        if c == 'b':
            if expectedStr == 'bob':
                bobcount = bobcount+1
        count=count+1
    print('Number of times bob occurs is: '+str(bobcount))

s = 'baxrdcjijezp'
# def longestAlphaSubString(s):
resStr=s[0:1]
count=1
previousLength=0
previousStr = ''
for c in s:
    compareStr = s[count:count+1]
    if c <= compareStr:
        if resStr == '':
            resStr = c + compareStr
        else:
            resStr=resStr+compareStr
    else:
        print('resStr : '+resStr)
        if len(resStr) > previousLength:
            previousLength = len(resStr)
            previousStr = resStr
        resStr = ''
    count=count+1
print('Longest substring in alphabetical order is:'+str(previousStr))
