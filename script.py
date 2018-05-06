import random

print("Password Generator! - By Nathan Waite")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('How many passwords would you like to be generated?')
number = int(number)

length = input('How many characters long should the password be?')
length = int(length)

print("List:")

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
