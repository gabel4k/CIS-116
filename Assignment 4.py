"""
Code must include a comment block that includes the following information
CIS 116 section 2095 22/FA
Gabriel Rose
9/29/2022
Assignment 4
Follow a series of prompts and receive inputs from the user to output the desired text.
"""

# Accept two integers and check whether they are equal or not.
print('Enter 2 integers to see if they are equal:')
intE1 = int(input('Int 1: '))
intE2 = int(input('Int 2: '))
if intE1 == intE2:
    print('Your numbers are equal.')
else:
    print('Your numbers are not equal.')

# Check whether a given number is even or odd.
intOE = int(input('\nEnter an integer: '))
if intOE % 2 == 0:
    print(intOE, 'is an even integer.')
else:
    print(intOE, 'is an odd number.')

# Check whether a given number is positive or negative.
intPN = int(input('\nEnter an integer: '))
print(intPN, 'is a positive number.') if (intPN > 0) else print(intPN, 'is a negative number.')

# Find whether a given year is a leap year or not.
year = int(input('\nEnter a year: '))
if year % 4 == 0:
    print(year, 'is a leap year.')
else:
    print(year, 'is not a leap year.')

# Read the age of a candidate and determine whether it is eligible for casting his/her own vote.
age = int(input('\nHow old are you?: '))
if age >= 18:
    print('Congratulations! You are eligible for casting your vote.')
else:
    print('You are not eligible for casting your vote.')

# Read the value of an integer m and display the value of n is 1 when m is larger than 0,
# 0 when m is 0 and -1 when m is less than 0.
m = int(input('\nEnter an integer: '))
if m > 0:
    n = 1
elif m == 0:
    n = 0
else:
    n = -1
print('The value of n is', n)

# Accept the height of a person in centimeter and categorize the person according to their height.
height = int(input('\nHow tall are you (in centimeters): '))
if height < 152:  # 5ft
    print('This person is short.')
elif height > 183:  # 6ft
    print('This person is tall.')
else:
    print('This person is average.')

# Find the largest of three numbers.
print('\nLets find the greatest number of three integers!')
int1 = int(input('Integer 1: '))
int2 = int(input('Integer 2: '))
int3 = int(input('Integer 3: '))
if int1 > int2 and int1 > int3:
    print('The 1st Number is the greatest among three.')
elif int2 > int1 and int2 > int3:
    print('The 2nd Number is the greatest among three.')
elif int3 > int2 and int3 > int1:
    print('The 3rd Number is the greatest among three.')
else:
    print('There is no number that is greatest among the three.')

# Create a match statement to output one of the following statements.
print('\nDo you have one of the following pets?: Fish, Dog, Cat, Squirrel')
pet = input('If so, what pet? If no, input "no": ')
match pet.upper():
    case 'FISH':
        print('You own a fish.')
    case 'DOG':
        print('You own a dog.')
    case 'CAT':
        print('You own a cat.')
    case 'SQUIRREL':
        print('You own a squirrel.')
    case other:
        print('You need a friend.')
