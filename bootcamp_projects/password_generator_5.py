#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("\nHow many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for _ in range(1, nr_letters + 1): # generate x amount of random letters 
  random_letter = random.randint(0, len(letters)) # generate random int for index
  password.append(letters[random_letter]) # adds the letter to the password list

for _ in range(1, nr_numbers + 1):
  random_numbers = random.randint(0,9)
  password.append(random_numbers)

for _ in range(1, nr_symbols + 1):
  random_symbols = random.randint(0, len(symbols))
  password.append(symbols[random_symbols])

random.shuffle(password)
new_password = ''.join(map(str,password))
print(f"\nHere is your password: {new_password}")



# alternative code
# password_list = []

# for _ in range(1, nr_letters + 1):
#   password_list += random.choice(letters)

# for _ in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# for _ in range(1, nr_symbols + 1):
#   password_list.append(random.choice(symbols)) #alt method

# random.shuffle(password_list) #shuffle the elements

# password1 = ""
# for char in password_list:
#   password1 += char

# print(f"\nHere is your password: {password1}")