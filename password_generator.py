#creating a password generator using for loop concept.
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','^','&','*','(',')','_']
print("welcome to the password generator")
nr_letters = int(input("how many letters would you like in your password ?\n"))
nr_numbers = int(input("how many numbers would you like in your password ?\n"))
nr_symbols = int(input("how many symbols would you like in your password ?\n"))
#easy level
import random
password = ""
for char in range(0,nr_letters):
    password += random.choice(letters)
#random.choice helps to select random chracters from a variable.
for char in range(0,nr_numbers):
    password += random.choice(numbers) 
for char in range(0,nr_symbols):
    password += random.choice(symbols)
print(password)




#hard level
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','^','&','*','(',')','_']
print("welcome to the password generator")
nr_letters = int(input("how many letters would you like in your password ?\n"))
nr_numbers = int(input("how many numbers would you like in your password ?\n"))
nr_symbols = int(input("how many symbols would you like in your password ?\n"))
import random
password_lists = []
# getting a list to store characters in a list.
for char in range(0,nr_letters):
    password_lists.append(random.choice(letters))
#append joins the rest chracters in the list.
for char in range(0,nr_numbers):
    password_lists.append(random.choice(numbers))
for char in range(0,nr_symbols):
    password_lists.append(random.choice(symbols))
random.shuffle(password_lists)
#random.shuffle(x) shuffle the chracters inside the list.
password1 = ""
for char in password_lists:
    password1 += char
print(f"your password is {password1}")