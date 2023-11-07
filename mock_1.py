### PART 1 - TASK 1 ###
def nearest_multiple_of_3(my_number):
    print(round(my_number/3) * 3)

nearest_multiple_of_3(24)

### PART 1 - TASK 2 ###
def check_value(my_value):
    if my_value < 10:
    	return "small"
    elif 10 <= my_value < 50:
    	return "medium"
    else:
    	return "large"

print(check_value(10))

### PART 1 - TASK 3 ###
def count_character_case_insensitive(my_word, capital_char, small_char):
    c = 0
    for i in my_word:
    	if i == capital_char or i == small_char:
    		c += 1

    return c

print(count_character_case_insensitive("Abracadabra", "a", "A"))

### PART 1 - TASK 4 ###
def sum_first_squares(number):
	if number < 0:
		return -1
	i = 0
	res = 0
	while i <= number:
		res += i ** 2
		i += 1

	return res

print(sum_first_squares( -5 ))

### PART 1 - TASK 5 ###
def check_double_char(string):
	for i in range(len(string) - 1):
		if string[i] == string[i+1]:
			return True
	else:
		return False


print(check_double_char("bkillompl"))

### PART 1 - TASK 6 ###
def return_values_below(my_list, threshold):
	res = []
	for i in my_list:
		if i < threshold:
			res.append(i)

	return res

print(return_values_below([ 34, 23, 26, 26, 27, 18, 60, 35, 59, 26 ], 30))