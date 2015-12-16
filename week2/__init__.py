__author__ = 'navneet'
x = 3
ans = 0
itersLeft = x
while(itersLeft != 0):
    ans = ans+x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' +str(ans))

'''
L3 Problem
'''

'''
num = 0
while num <= 5:
    print num
    num += 1

print "Outside of loop"
print num

print '   '

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print "Number of apples: " + str(numberOfApples)

num = 10
while num > 3:
    num -= 1
    print num
print '    '

num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop'

print '    '
num = 100
while not False:
    if num < 0:
        break
print 'num is: ' + str(num)
'''


'''
L3 Problem 2A
'''
num = 2
while(num <= 10):
    print(num)
    num = num + 2
print 'Goodbye!'

print '     '

'''
L3 Problem 2C
'''

end = 6
result = 0
while(end >= 0):
    result = result + end
    end = end - 1
print(result)












