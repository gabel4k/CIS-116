"""
Create a python script that will input variables necessary to complete the following expressions and output the following text.
               quit the program if the python version is not 3
              Create a Dictionary Data type containing the cost of Regular, Mid grade, and Premium gas
              Create a List data containing 6 user entered values
                        Remove the 3rd value
               Create a Tuple that contains the colors of the rainbow.
               Set a Boolean variable to True if the user enters a T when prompted., otherwise set it to False
              Output.
                    All Floats must be set to 2 decimals
                    All user name output must be in all capital letters
               "Good Morning <<user name>> the cost to fill your gas tank with <<Chaose gas type>> is <<Cost to fill tank>>"
               "The union of 2 sets contains the value <<union of sets>>"
               "The value in position <<position>> of the Tuple is <<Tuple Value>>"

Code must include a comment block that includes the following information
CIS 116 section 2095 22/FA
Gabriel Rose
9/21/2022
Assignment 3
A python script that will input variables necessary to complete expressions and output the required text.
"""

# Check for version Python 3+
import sys
if sys.version_info < (3, 0):
    sys.exit("Please use Python 3.0+")


userName = input('What is your name?: ')

# Cost of Gas Types
costR = float(input('Regular gas price: '))
costM = float(input('Mid grade gas price: '))
costP = float(input('Premium gas price: '))
tankGallons = float(input('How many gallons can your tank hold?: '))
# Dictionary of Prices
gasPrices = {'Regular': costR, 'Mid grade': costM, 'Premium': costP}
gasTypes = ['Regular', 'Mid grade', 'Premium']

inputList = [input('Input any value: '), input('Input any value: '), input('Input any value: '),
             input('Input any value: '), input('Input any value: '), input('Input any value: ')]
# Remove the 3rd value of inputList
inputList.pop(2)

# Rainbow tuple and position input
rainbowColors = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
position = int(input('Input a number 1-7: '))
while position < 1 or position > 7:
    position = int(input('Incorrect number. Input a number 1-7: '))

# 2 sets for union prompt
set1 = {inputList[0], inputList[1], inputList[2], inputList[3], inputList[4]}
set2 = {"set", "more set", "and more", "set"}
set3 = set1.union(set1, set2)

# T Boolean
if input('Input the letter "T": ') == 'T':
    boolT = True
else:
    boolT = False

# Output
print(f'\nGood morning {userName.upper()}.')
print(f'The cost to fill your gas tank with {gasTypes[0]} is {tankGallons * gasPrices["Regular"]:.2f}.')
print(f'The cost to fill your gas tank with {gasTypes[1]} is {tankGallons * gasPrices["Mid grade"]:.2f}.')
print(f'The cost to fill your gas tank with {gasTypes[2]} is {tankGallons * gasPrices["Premium"]:.2f}.')
print(f'The union of 2 sets contains the values: {set3}.')
print(f'The value in position {position} of the Tuples is {rainbowColors[position-1]}.')
