# When a user types a number of inches into a prompt,
# we will convert this user input from inches into 
# feet and return the result to the user
def inches_to_feet(userinput):
	# variable declaration (Not necessary in Python)
	#value_in_inches = 0
	#value_in_feet = 0
	# assigns value inputted by user to the value_in_inches variable
	# example: user types 8. value_in_inches becomes 8
	value_in_inches = userinput
	# There are 12 inches in 1 foot.  This converts inches to feet
	value_in_feet = (value_in_inches / 12)
	# After the function runs, we will return to the outside of the function the value_in_feet
	return value_in_feet

def feet_to_inches(userinput):
	value_in_feet = 0
	value_in_inches = 0
	value_in_feet = float(userinput)
	value_in_inches = (value_in_feet * 12)
	return value_in_inches

def miles_to_kilometers(userinput):
	value_in_miles = 0
	value_in_kilometers = 0
	value_in_miles = float(userinput)
	value_in_kilometers = (value_in_miles * 1.60934)
	return value_in_kilometers

def kilometers_to_miles(userinput):
	value_in_kilometers = 0
	value_in_miles = 0
	value_in_kilometers = userinput
	value_in_miles = (value_in_kilometers * .621371)
	return value_in_miles

def conversion_picker(user_picks_conversion):
	if (user_picks_conversion == 1):
		print("You selected Inches to feet")
		user_chose_inches_to_feet = True
		userinput = input("Please type the number of inches and press ENTER\n")
		result = inches_to_feet(float(userinput))
		print(result)
	elif (user_picks_conversion ==2):
		print("You selected Feet to inches")
		user_chose_feet_to_inches = True
		userinput = input("Please type the number of feet and press ENTER\n")
		result = feet_to_inches(float(userinput))
		print(result)
	elif (user_picks_conversion ==3):
		print("You selected Miles to kilometers")
		user_chose_miles_to_kilometers = True
		userinput = input("Please type the number of miles and press ENTER\n")
		result = miles_to_kilometers(float(userinput))
		print(result)
	elif (user_picks_conversion == 4):
		print("You selected Kilometers to miles")
		user_chose_kilometers_to_miles = True
		userinput = input("Please type the number of kilometers and press ENTER\n")
		result = kilometers_to_miles(float(userinput))
		print(result)
	else:
		print("I did not recognize that selection.")