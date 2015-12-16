__author__ = 'navneet'

# num = 256
# if num < 0:
#     isNeg = True
#     num = abs(num)
# else:
#     isNeg = False
# result = ''
# if num == 0:
#     result = '0'
# while num > 2:
#     result = str(num % 2)  + result
#     num = num / 2
# if isNeg:
#     result = '-' + result
# print 'result is : '+result

'''
Guesses to find cube root
'''

# x = 25
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# while(abs(ans**2 - x)) >= epsilon and ans <= x:
#     ans += step
#     numGuesses += 1
# print('numGuesses = '+str(numGuesses))
# if abs(ans**2-x) >= epsilon:
#     print('Failed on square root of '+str(x))
# else:
#     print(str(ans)+' is close to square root of '+str(x))
#
# print '####'
# x = 23
# epsilon = 0.01
# step = 0.1
# guess = 0.0
#
# while abs(guess**2-x) >= epsilon:
#     if guess <= x:
#         guess += step
#     else:
#         break
#
# if abs(guess**2 - x) >= epsilon:
#     print 'failed'
# else:
#     print 'succeeded: ' + str(guess)



print 'Please think a number between 0 and 100!'
# found = True
# while found:
#     num = raw_input('Please think a number between 0 and 100!')
#     if num.isdigit():
#         found = False
# if(num < 0):
#     print'Enter number between 0 and 100'
# if(num >= 100):
#     print'Enter number between 0 and 100'
low = 0
high = 100
mid = (low+high)/2
found = True
while(found):

    enter_char = (raw_input("Is your secret number "+str(mid)+ " ?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if not ((enter_char == 'c') or (enter_char == 'l') or (enter_char == 'h')):
        print 'Sorry, I did not understand your input.'

    # if num == mid:
    if enter_char == 'c':
        print 'Game over. Your secret number was: '+str(mid)
        found=False
    # if num > mid:
    if enter_char == 'h':
        low=mid
        mid = (low+high)/2
    # if num < mid:
    if enter_char == 'l':
        high=mid
        mid = (low+high)/2








