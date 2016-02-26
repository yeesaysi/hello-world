import conversions

print("""
	This python script will convert units based on your input.  Currently, we
	can convert the following units:
	""")
print("""
	\t1 Inches to feet
	\t2 Feet to inches
	\t3 Miles to kilometers
	\t4 Kilometers to miles
	Please type the number of the conversion you would like to perform and
	press ENTER
	""")

user_picks_conversion = int(input())

user_chose_inches_to_feet = False
user_chose_feet_to_inches = False
user_chose_miles_to_kilometers = False
user_chose_kilometers_to_miles = False




conversions.conversion_picker(user_picks_conversion)