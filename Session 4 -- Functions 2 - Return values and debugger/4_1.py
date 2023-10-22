# 1.1
def average(a, b):
	print((a + b) / 2)
average(10, 5)

# 1.2
def average(a, b):
	return (a + b) / 2
average(10, 5) # return enstores
print(average(10, 5)) # 1.3
print("#"*20)

# 2.1
import lab4_ex2_start
lab4_ex2_start.inch_to_cm(20)
lab4_ex2_start.calc_price("thin", 50.8)

# 2.2
result = lab4_ex2_start.re_inch_to_cm(20)
lab4_ex2_start.calc_price("thin", result)
print("#"*20)

# 3
def F_to_C(F):
	return (F - 32) / 1.8

def alert_user(C):
	if C >= 100:
		return "Water is boiling"
	elif 85 <= C <= 90:
		return "Ready to make tea"
	elif 40 <= C <= 45:
		return "Perfect for a foot bath"
	else:
		return f"Current water temperature is {C}°C"

temp_converted_to_C = F_to_C(110)
print(alert_user(temp_converted_to_C))

# 4