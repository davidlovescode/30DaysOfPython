#Day 2:30 Days of python programming

#Level 1
first_name = 'Tripple'
last_name = 'T'
full_name = first_name + ' ' + last_name
country = 'Ohio'
city = 'Morioh'
age = 19
year = 2024
is_married = False
is_true = True
is_light_on = False
height, weight, BMI = 5.9, 160, 23.6

#level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))    
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(height))
print(type(weight))
print(type(BMI))

print(len(first_name))

if len(first_name) > len(last_name):
    print("first_name is longer")
elif len(first_name) < len(last_name):
    print("last_name is longer")
else:
    print("Both strings have equal length")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius ** 2

radius = int(input("Enter the radius of a circle: "))
area_of_circle = 3.14 * radius ** 2
print("The area of the circle is: ", area_of_circle)

first_name, last_name, country, age = input("Enter your first name, last name, country and age separated by comas: ").split(",")
