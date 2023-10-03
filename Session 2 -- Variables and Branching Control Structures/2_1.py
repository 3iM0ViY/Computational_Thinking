# 1.1
name = "Jesus Christ"
age = 33
print(f"{name} - {age} years old")
# 1.2
age += 1
print(f"{name} - {age} years old")
print("#"*20)

# 2
pi = 3.14
radius = 10
area = pi * radius**2
print("Area:", area)
circumference = 2 * pi * radius
print("Circumference:", round(circumference, 3))
print("#"*20)

# 3
while True:
	floor = str(55)
	floor_1 = input("write your floor or type q for exiting the loop: ")
	if floor_1 == floor:
		print("DING!")
	if floor_1 == "q":
		break
print("#"*20)

# 4
name = input("Type your name: ")
if len(name) < 4:
	name = name + name
print("Username:", name)
print("#"*20)

# 5
print("#5")
pi = 3.14
while True:
	radius = input("Your radius: ")
	try:
		radius = int(radius)
		if radius > 0:
			area = pi * radius**2
			print("Area:", area)
			circumference = 2 * pi * radius
			print("Circumference:", round(circumference, 3))
		else:
			print("No negative radius!!!")
	except:
		pass
	if radius == "q":
		break
print("#"*20)

# 6
print("#6")
while True:
	pi = input("Ex.6 Your pi: ")
	try:
		pi = float(pi)
		if (3.1 < pi < 3.2) and (round(pi % 0.1, 7) > 0.01):
			radius = input("Your radius: ")
			radius = int(radius)
			if radius > 0:
				area = pi * radius**2
				print("Area:", area)
				circumference = 2 * pi * radius
				print("Circumference:", round(circumference, 3))
			else:
				print("No negative radius!!!")
		else:
			print("Be adequate with your pi!!!")
			continue
	except:
		pass
	if radius == "q" or pi == "q":
		break
print("#"*20)

# 7
while True:
	number = input("Natural number: ")
	if number == "q":
		break
	try:
		number = int(number)
		number_was_even = bool(number % 2) # 6.3 & 6.4
		if number_was_even:
			print("Odd!")
		else: 
			print("Even!")
	except:
		print("Do a number!!!")


print("#"*20)

# 8
age = 10
if age < 0:
    message = "error - age < 0"
elif age < 18:
    message = "you are a minor"
else:
    message = "you are an adult"
print(message)

number = 12
if number % 2 == 0:
    print(number, "is even")
if number % 3 == 0:
    print(number, "is divisible by 3")
print("#"*20)

# 9
floor = 0
min_f = 0 # 9.2
max_f = 60
if floor < min_f: print("To the center of the Earth!!!")
elif floor > max_f: print("To the Moon!!!")
elif floor == min_f or floor == max_f: print("Ding!")
elif floor % 10 == 0: print(floor)
print("#"*20)

# 10
a, b, c = -4, 7, -10
a, b, c = -4, 7, 5
a, b, c = -4, 7, 6
a, b, c = 10, 7, 6 # no definition in condition.1

if a > 0:
    if b == 7:
        c = c + 1
    elif b == 8:
        if c < 0:
            c = 0
        else:
            c = a + b
else:
    a = 0
    if c < 0:
        d = "c is negative"
    elif c == 0:
        d = "c is zero"
    else:
        d = "c is positive"
        if c < 10:
            d = d + " , but smaller than 10"
            if c % 2 == 0:
                d = d + " and even"
            if c % 3 == 0:
                d = d + " and divisible by 3"
            else:
                d = d + " and not divisible by 3"                              
if a == 0: 
    c = 100
    a = -a
b = 200

print(f"a: {a}; b: {b}; c: {c}; d: {d}")