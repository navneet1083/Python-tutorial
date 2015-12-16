####
# Lists 'index' their entries based on the position in the list
# Dictionaries are like bags - no orders
# So we 'index' the things we put in the Dictionary with a 'lookup tag'
####
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse
print purse['candy']
# Adding values
purse['candy'] = purse['candy'] + 5
print purse

## Also declared as literals
listDict = {}
# empty dict literals
print listDict

listDict = {'chuck':1,'fred':42,'jan':100}
print listDict

# looking for key that does not exists (traceback)
# print listDict['test']

print 'test' in listDict

def countNames():
    counts = dict()
    names = ['csev','cwen','csev','zgijan','cwen']
    for name in names:
        if name not in counts:
            counts[name] = 1
        else:
            counts[name] = counts[name] + 1
    print counts

# Simplified for above (countNames)
def simplifiedCountNames():
    counts = dict()
    names = ['csev','cwen','csev','zgijan','cwen']
    for name in names:
        counts[name] = counts.get(name, 0)+1
    print 'From simplified :',counts


# 'get' method for dictionary
def getCounts(name, counts):
    if name in counts:
        print counts[name]
    else:
        print 0



#countNames()
counts = {'csev':2,'zgijan':1,'cwen':2}
getCounts('csev',counts)
print '******'
print counts.get('csev2',-1)
# simplifiedCountNames()


# Definite Loops and Dictionaries
counts = {'chuck':1,'fred':42,'jan':100}
for name in counts:
    print name,counts[name]


# Retrieving lists of keys and values
print 'List :',list(counts)
print 'Keys :',counts.keys()
print 'Values :',counts.values()
print 'Items :',counts.items()  ## basically it's a tuple

# Two iteration variables
for name,count in counts.items():
    print 'name :',name
    print 'value : ',count


def countMostFreqWords():
    name = raw_input('Enter a file name :')
    handle = open(name, 'r')
    text = handle.read()
    words = text.split()

    counts = dict()
    for word in words:
        counts[word] = counts.get(word,0)+1

    bigWord = None
    bigCount = None
    for word,count in counts.items():
        if bigCount is None or count > bigCount:
            bigWord = word
            bigCount = count