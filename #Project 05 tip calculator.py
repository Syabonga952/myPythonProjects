print("Welcome to the tip calculator.")
#ask the user how much is the bill
bill = float(input("How much is the bill? $\n"))
# ask the user how much they want to tip in %
tip = input("How much do you want to tip?\n")
calculated_tip = tip / 100
#ask the user how many they are
people = int(input("How many of you are spliting the bill?\n"))
#calculate how much each person sould pay
each_person = bill * calculated_tip
total_tip = bill + each_person
split_bill = total_tip / people
# round off the bill for each person
rounded_results = round(split_bill,2)
# print the bill 
print(f"Each person should pay : ${rounded_results} of their share of the bill")