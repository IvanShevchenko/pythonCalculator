varList = input()
num1, op, num2 = varList.split(" ")

num1 = float(num1)
num2 = float(num2)

def calc():
	if op == "+":
		print("Answer: ", num1 + num2)
	elif op == "-":
		print("Answer: ", num1 - num2)
	elif op == "*":
		print("Answer: ", num1 * num2)
	elif op == "/":
		print("Answer: ", num1 / num2)
	else:
		print("Invalid Operator")

calc()