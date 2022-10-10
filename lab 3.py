#task1
name = input("what is your name")
if name == "":
    print("hello stanger")
else:
    print(" hello " + name + ' nice to meet you')

 #task2two5
 password = input("enter  password")
 password2 = input("confirm password")
if password1 == password2:
     print("password is correct")
 else:
     print("wrong password")
#3

password = input("What is your password? ")
PasswordLength = len(password)
password2 = input("confirm password")
if PasswordLength <= 12:
    print(f'Your password is {password}')
elif PasswordLength >= 12:
    print("password is too long! (MAXIMUM IS 12 CHARACTERS)")
if PasswordLength >= 8:
    print(f'Your password is {password}')
elif PasswordLength <= 8:
    print("password is too short! (MINIMUM IS 8 CHARACTERS)")
#4
BAD_PASSWORDS = ['password', '12345678',]
for i in BAD_PASSWORDS:
    if password == BAD_PASSWORDS :
        print("your password is too weak try a different password")
#5
y_input = raw_input("Enter password ")
if len(my_input) > 3:
  print ("More then 3")
else:
  print ("Ok")

  #6
  num = 7

  for i in range(1,11):
      print(num, 'x' , i, num*i)

#7
 num = input("what times table number would you like?")
  for i in range(1,11):
      print(num, 'x' , i, num*i)

#8
num = 7

for i in range(11, 1):
    print(num, 'x', i, num * i)