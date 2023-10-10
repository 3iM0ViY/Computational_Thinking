# 1
def hello_function(name):
	print("Hello,", name)

hello_function("Nigel")
print("#"*20)

# 2
def hello_to(name, place):
	print(f"Hello, {name}, and welcome to {place}!")

hello_to("Nigel", "Group T")
print("#"*20)

# 3
def calculate_area(r):
	pi = 3.14
	area = pi * r**2
	print("Area:", area)

calculate_area(5)
print("#"*20)

# 4
def greet_based_on_name_length(name):
	if len(name) < 4:
		print(f"Hello {name}, you have a short name")
	else:
		print(f"Hello {name}, you have quite a long name")

greet_based_on_name_length("Yulian")
print("#"*20)

# 5
def greet_based_on_name_length(name, length):
	if len(name) < length:
		print(f"Hello {name}, you have a short name")
	else:
		print(f"Hello {name}, you have quite a long name")

greet_based_on_name_length("Yulian", 9)
print("#"*20)

# 6
def greet_full_or_not(name, full = False):
	if full:
		print(f"Hello {name}, I hope you have a pleasant day")
	else:
		print("Hello,", name)

greet_full_or_not("Yulian", True)
print("#"*20)

# 7
def calculate_fine(alcho):
	fine = 0
	try:
		if 0 <= alcho <= 1:
			if 0.5 <= alcho <= 0.8:
				fine += 50
			elif 0.8 < alcho <= 1.5:
				fine = 50 + (((alcho - 0.8) / 0.7) * 100)
			elif alcho > 1.5:
				fine = 250
				print("You gonna die...")
			print(f"Fine: {fine}")
		else:
			raise
	except:
		print("You so drunk that can't choose ok numbers?!")

calculate_fine(-2)
print("#"*20)

# 8.1
def movie_access(age, adults):
	if adults:
		if age >= 18:
			print("Welcome!")
		else:
			print("Please, leave")
	else:
		print("Welcome to this family movie!")

movie_access(18, False)

# 8.2
def movie_access(age, adults):
	if adults and age >= 18:
		print("Welcome!")
	elif adults:
		print("Please, leave")
	else:
		print("Welcome to this family movie!")

movie_access(17, True)