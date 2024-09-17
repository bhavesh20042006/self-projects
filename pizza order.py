print("welcome to python pizza deliveries")
bill = 0
size = input("what size pizza do you want? s,m or l? ")
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("you typed wrong inputs")
pepperoni = input("do you want pepperoni on your pizza ? y or n ")
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
extra_cheese = input("do you want extra cheese ? y or n ")
if extra_cheese == "y":
    bill += 1
print("your final bill is ", bill)