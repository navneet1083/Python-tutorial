__author__ = 'navneet'

# x = int(raw_input('Enter an integer :'))
# ans = 0
# while(ans**3 < abs(x)):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(str(x) + ' is not a perfect cube.')
# else :
#     if x < 0:
#         ans = -ans
#     print('Cube root of '+str(x)+' is : '+str(ans))


'''
For loops
'''
# for num in range(10):
#     print(num)
# print('value outside for loop : '+str(num))

# x = int(raw_input('Enter an integer : '))
# ans = 0
# for num in range(0, abs(x)):
#     if num**3 > abs(x):
#         break
#     ans = num
# if ans**3 == abs(x):
#     if x < 0 :
#         ans = -ans
#     print('Cube root of ' + str(x)+' is : '+str(ans))
# else :
#     print(str(x) + ' is not a perfect cube.')


# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print char
#     else:
#         numCons -= 1
#
# print 'numVowels is: ' + str(numVowels)
# print 'numCons is: ' + str(numCons)
#
# for variable in range(20):
#     if variable % 4 == 0:
#         print variable
#     if variable % 16 == 0:
#         print 'Foo!'
#
# for letter in 'hola':
#     print(letter)
#
# print('     ')
# count = 0
# for letter in 'Snow!':
#     print 'Letter # ' + str(count) + ' is ' + str(letter)
#     count += 1
#     break
# print count

for num in range(2,11,2):
  print(num)
print 'Goodbye!'

print '      '

print 'Hello!'
for newNum in range(10,0,-2):
  print(newNum)



print('####')

end = 6
ans = 0
for num in range(0,end+1):
    ans = ans + num
print(ans)


iteration = 0
count = 0
while iteration < 5:
    count = 0
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

print ' ##### '
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

print '#####'

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

print 'testing'
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)