num1 = float(input("First Number: "))
op = (input("Operator: "))
num2 = float(input("Second Number: "))

def calc():
	if op == "+":
		print("Answer: ", num1 + num2)
	elif op == "-":
		print("Answer: ", num1 - num2)
	elif op == "*":
		print("Answer: ", num1 * num2)
	else:
		print("Answer: ", num1 / num2)

calc()