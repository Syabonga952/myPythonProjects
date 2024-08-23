#how to calculate the Body Mass Index of a person
# ask the user to enter their body mass
body_mass = input("What is your body waight?\n")
# ask the user their body height
body_height = input("What is your body height?\n")
# now calculate the users BMI
BMI = int(body_mass/ (body_height)**2)
# print out the users BMI
print(str("Your BMI is" + (BMI)))
