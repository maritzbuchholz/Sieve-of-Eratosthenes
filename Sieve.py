## getting an input
def get_nat_num():
	error_message =  "Sorry. A valid input is a whole number greater than 1.\n"
	while True:
		user_input = raw_input("\nPlease enter a natural number greater than 1: ")		
		try:
			nat_num = int (user_input)
			if nat_num > 1:
				print "Great, the input is good!\n"
				return nat_num
				break
			else:
				print error_message
		except ValueError:
			print error_message
		

## the sieve		
def sieve(nat_list, next_item, last_item):
	dummy_list = []
	for i in nat_list:
		dummy_variable = next_item * i
		if dummy_variable <= last_item:
			dummy_list.append(dummy_variable)
		else:
			break
	return dummy_list
			
def find_prime_numbers(nat_list):
	
	return_list = list(nat_list)
	
	k = 0
	
	while return_list[k] != return_list[-1]:
		dummy_list = sieve(nat_list, return_list[k], return_list[-1])
		for i in dummy_list:
			try:
				return_list.remove(i)
			except ValueError:
				pass

		k += 1

	return return_list

## the program in a loop that the user can quit
def run_program():
	while True:	
		user_nat_num = get_nat_num()
		user_nat_list = range (2, user_nat_num + 1)
		prime_num = find_prime_numbers(user_nat_list)
		print "Here are your prime numbers!:", prime_num, "\n"
		raw_input("To continue, press enter. To quit, press CTRL-C")

run_program()
	
