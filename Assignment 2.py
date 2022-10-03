# CIS 116 section 2095 22/FA
# Gabriel Rose
# 9/15/2022
# 2
# Create a python script that will input variables necessary to find the area of a triangle, 
# diameter of a circle, and the age of Ryder.

print('Input the following...')
print('Your name: ')
name = input()

print('Triangle Base: ')
triBase = float(input())

print('Triangle Hight: ')
triHight = float(input())

print('Circle Radius: ')
radius = float(input())

print('Age of dog (human years): ')
humanYears = float(input())

print()
print(name)
print('The Area of a Triangle is', f'{(triBase / 2) * triHight:.2f}')
print('The Diameter of a circle is', f'{2 * radius:.2f}')
print('The good boy, Ryder, is', f'{humanYears * 7:.2f}')
quit()
