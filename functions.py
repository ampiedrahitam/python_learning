# def greet():
#     print('Hi fren!')

# greet()

# def greet(age,name):
#     print(f'Subject1, age {age} name {name}')

# age = input('Type in your age  ')
# name = input('Type in your name  ')

# greet(age, name)

# def new(area):
#     print('Thea area of your circle is', str(area))

# radius = input('Please enter the radius of your circle (m): ')
# area = 3.1428 * int(radius)**2

# new(area)

def area(radius):
 return 3.1428*radius*radius

def volume(area, length):
    print(area*length)

radius = int(input('Please enter the radius:  '))
length = int(input('Please enter the length:  '))

volume(area(radius),length)