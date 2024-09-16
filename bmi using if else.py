weight = int(input("enter your weight ? "))
height = float(input("enter your height ? "))
bmi = weight/(height**2)
if bmi > 18.5 :
    print("underweight")
elif bmi >= 18.5 and bmi <= 25:
    print("normalweight")
else:
    print("overweight")