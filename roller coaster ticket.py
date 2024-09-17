# roller coaster 
# condition 2 pay the ticket price according to the age.
# condition 3 print photos for the ride.
# condition 4 freee tickets for people suffering from midlife crises(45 - 55).
print("welcome to the roler coaster!")
height = float(input("what is your height in cm: "))
age = int(input("what is your age: "))
if height >= 120:
    if age > 18:
        bill = 5
        print("please pay $5.")
    elif age >= 12 and age <= 18:
        bill = 7
        print("please pay $7.")
    elif age >= 45 and age <= 55:
        print("everything is going to be okay have a free ride on us!")
    else:
        bill = 5
        print("please pay $5.")
    print("you can ride the roller coaster")
    want_photo = input("do you wanr the photo to be taken?yes or no ? ")
    if want_photo =="yes":
        print("please pay " ,bill + 5)
    else:
        print("please pay " , bill)

else:
    print("sorry you have to grow taller before you ride.")