print("Welcome to the tip calculator !")
total_bill = int(input("what was the total bill?"))
tip = int(input("how much tip would you like to give ?10,12,or15"))
people = int(input("how many people to split the bill with?"))
bill_with_tip = total_bill*(tip/100) + total_bill
bill_after_spliting = bill_with_tip/people
print("each person should pay" , round(bill_after_spliting , 1))
