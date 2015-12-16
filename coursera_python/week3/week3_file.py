def printMyName(s):
    print 'name entered is : ',s


# File Operations

def countLines(fileName) :
    fhand = open(fileName)
    count = 0
    for line in fhand:
        count = count + 1
    print 'Total line count of file is : ',count

# Short operation for reading whole file (it works with small files)
def readSmallFiles(smallFileName):
    fhand = open(smallFileName)
    rFile = fhand.read()          # read the whole file into memory
    print 'Number of characters in a small file is ', len(rFile)


# Searching through file
def searchInFile(fileName):
    fhand = open(fileName)
    for line in fhand:
        if line.startswith("AUS"):
          line = line.rstrip()
          print 'line',line

# catching exception
def elegantFileOpen(fileName):
    try:
        fhand = open(fileName)
    except:
        print 'File can not be opened: ', fileName
        exit()
    count = 0
    for line in fhand:
        count = count + 1
    print 'Total number of lines in file is: ',count

def printContentsTOUpper(fname):
    try:
      fh = open(fname)
    except:
      print 'File can not be opened:',fname
      exit()

    for line in fh:
      line = line.rstrip().upper()
      print line


fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File can not be opened:'
    exit()

for line in fh:
    line = line.rstrip().upper()
    print line



# countLines('/Users/navneet/file.csv')
# searchInFile('/Users/navneet/file.csv')
# printContentsTOUpper('/Users/navneet/PROJECTS/EDX/Python-tutorial/coursera_python/week3/sample.txt')
