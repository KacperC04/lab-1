#task 1
name = input("hello what is your name?")
print("hello, "+ name +" its nice to meet you")

#task 2
Fahrenheit_1 = float(input("Temperature value in degree Fahrenheit: "))

# For Converting the temperature from degree Fahrenheit to degree Celsius
# by using the above given formula
celsius_1 = (Fahrenheit_1 - 32) / 1.8

# Print the result
print('The %.2f degree Fahrenheit is equal to: %.2f Celsius'
      % (Fahrenheit_1, celsius_1))
#task 3
num_of_students = int(input("how many students are there?"))
num_of_group: = int(input("what is the group size?"))
print(num_of_students / num_of_group)
#task 4
num_of_sweets = int(input("how many sweets are there?"))
number_of_pupil = int(input("how many numnber of pupils are there?"))
print( number_of_pupil / num_of_sweets)