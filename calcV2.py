from sys import argv

filename, num1, op, num2 = argv

num1 = float(num1)
num2 = float(num2)

def calc():
	if op == "+":
		print("Answer: ", num1 + num2)
	elif op == "-":
		print("Answer: ", num1 - num2)
	elif op == "x":
		print("Answer: ", num1 * num2)
	else:
		print("Answer: ", num1 / num2)

calc()