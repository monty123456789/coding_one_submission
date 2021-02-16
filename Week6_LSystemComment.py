# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}

def l_system(initial, rules, generation):
	# Function declaration with 3 arguments. Initial argument is the string to be used by the function, the rules argument are the rules which will effect the string, and the generation argument is the number of times the function will run on the string. 
	current = initial
	#reassigning the string the the variable 'current'

	for _ in range(0, generation):
		#This for loop determines how many times the function will run the rules on the string. 
		result = ""
		# creates an empty string which the result of the function can be appended to. 
	

		for state in current:
			# initial string which has been reasigned to current is looped through. 

			result += rules.get(state, state)
			#rules are called on the result of the for loop, and if the result is not in the rules, the result is left. These results are appended to the empty 'result' variable. This loop runs as many times as the above for loop runs. 

		current = result
		#current is reassigned. 

	return current

for i in range(0, 10):
	#Determines the number of times the function will run the rules on the string. 
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
	#The space between the {} is the string. Values are added inside the {} with the .format. 
	#.format is divided by a comma, everything before the comma goes to the first {}, everytying after to the second. 
	#The runction is called with i as the generation, so each loop becomes larger as the for loop runs. 
