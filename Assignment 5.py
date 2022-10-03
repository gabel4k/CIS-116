"""
Code must include a comment block that includes the following information
CIS 116 section 2095 22/FA
Gabriel Rose
10/03/2022
Assignment 5
Follow a series of prompts and receive inputs from the user to output the desired text.

Using a single character at a time create loops to  Print the following patterns:
Pattern 1:
*
**
***
****
Pattern 2
  *
 ***
*****
 ***
  *
Pattern 3
1010101
 10101
  101
   1
Create a tuple that contains the following values and use a loop display the values.
car
boat
fish
cat
floss
toothbrush
Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
Print average and product of all numbers.
"""


# Pattern Function
def patternFun(spaceNum, chrNum, chrct):  # Number of spaces, number of characters, character value
    x = len(chrct)
    y = 0
    while spaceNum > 0:
        spaceNum -= 1
        print(' ', end='')
    while chrNum > 0:
        chrNum -= 1
        print(chrct[y], end='')
        if x > 1 and x - 1 == y:
            y = 0
        elif x > 1:
            y += 1
    print('')


# Pattern 1
print('Pattern 1:')
patternFun(0, 1, '*')
patternFun(0, 2, '*')
patternFun(0, 3, '*')
patternFun(0, 4, '*')

# Pattern 2
print('\nPattern 2:')
patternFun(2, 1, '*')
patternFun(1, 3, '*')
patternFun(0, 5, '*')
patternFun(1, 3, '*')
patternFun(2, 1, '*')

# Pattern 3
print('\nPattern 3:')
patternFun(0, 7, '10')
patternFun(1, 5, '10')
patternFun(2, 3, '10')
patternFun(3, 1, '10')

# Create a tuple that contains the following values and use a loop display the values.
print('')
myTup = ('car', 'boat', 'fish', 'cat', 'floss', 'toothbrush')
for x in myTup:
    print(x)

# Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print average and product of all numbers.
sum = 0
inNum = 0
userIn = ''
print('\nEnter a series of integers and I\'ll calculate the average. When finished, enter "q" without the quotations.')
while userIn != 'q':
    userIn = input('Enter an integer (or "q" to quit): ')
    if not userIn.isalpha():
        sum += int(userIn)
        inNum += 1
    elif userIn != 'q':
        print('That\'s not a number or "q" ya goof.')

print('\nYour average is', sum/inNum)
