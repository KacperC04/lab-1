#1
print("what is your number")
number = range(1,100)
if number in range:
    print("true")
else:
    print('False')


#task2
def up_low(string):
  uppers = 0
  lowers = 0
  for char in string:
    if char.islower():
      lowers += 1
    elif char.isupper():
      uppers +=1
    else: #I added an extra case for the rest of the chars that aren't lower non upper
      pass
  return(uppers, lowers)

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))


#task3
s = input("")
print("original string:")
print(s)
print("after cpaitalizing first letter:")
print(s.capitalize())


#task 4
my_str = input("")
result = my_str.rstrimp(my_str[-1])


#task5
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")


#task7
#Create a set
from operator import lt, gt
def ultimate (l,op,c=1,u=0):
    try:
        if op(l[c],l[u]):
            u = c
        c += 1
        return ultimate(l,op,c,u)
    except IndexError:
        return l[u]
def minimum (l):
    return ultimate(l,lt)
def maximum (l):
    return ultimate(l,gt)

from statistics import mean, median

somelist =  [1,12,2,53,23,6,17]
avg_value = mean(somelist)
median_value = median(somelist)


#task8
