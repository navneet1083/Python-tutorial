friends = ['Joseph','Glenn','Sally']
carryon = ['socks','shirts','perfume']
num = [2,4,8]
print friends
print carryon
print num
allcomb = ['red',24, 56.7899999999]
print allcomb
print friends[1]
print friends[0]


# length of list
x = [1,2,'joe',99]
print len(x)

# range function - it generates a list
print range(4)
print len(friends)
print range(len(friends))

for friend in friends:
    print 'Happy New Year : ',friend

for i in range(len(friends)):
    friend = friends[i]
    print 'Happy New Year : ',friend

# Concatenating list '+'
a = [1,2,3]
b = [5,6,7]
c = a + b
print a + b
print c
print a

# list method
x = list()
type(x)
dir(x)

# Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print stuff
stuff.append('cookie')
print stuff

# Is something in list (look for an element)
some = [1,9,21,10,16]
print 9 in some
print 15 in some
print 20 not in some

# list is an ordered
print friends
friends.sort()
print friends

# built-in functions and lists
nums = [3,41,12,9,74,15]
print max(nums)
print min(nums)
print len(nums)
print sum(nums)
print sum(nums)/(len(nums)+2)

# calculating average within a list
def sumList():
    numlist = list()
    while True:
        inp = raw_input('Enter a number : ')
        if inp == 'done' : break
        value = float(inp)
        numlist.append(value)
    average = sum(numlist)/len(numlist)
    print 'Average:',average

# Strings and list
abc = "with three words"
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
for w in stuff:
    print w

line = "A lot             of spaces"
etc = line.split()
print etc
line = 'first;second;third'
print line
print len(line)
thing = line.split(";")
print thing
print thing[0]


print 'reading file'

def assign2(fname):
    fh = open(fname)
    lst = list()
    for line in fh:
        spl = line.rstrip().split()
        for word in spl:
            if word not in lst:
                lst.append(word)
    lst.sort()
    print lst

def assign3(fname):
    lst = list()
    fh = open(fname)
    for line in fh:
        # line =  line.rstrip()
        if line.startswith('From '):
            count = count + 1
            spl = line.split()[1]
            lst.append(spl)
            print spl
    print "There were", len(spl), "lines in the file with From as the first word"


# assign2('romeo.txt')
assign3('mbox-short.txt')