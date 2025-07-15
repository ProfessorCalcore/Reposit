while True:
	
	def mathNumbers():
		print("Calculator initiated ")
		num1 = int(input("Enter number "))
		mathsymbol = input(f"+, ÷, ×, -")
		num2 = int(input("Enter number "))
	#===============================#
		if mathsymbol == "+":
			result = num1 + num2
			print(result)
			
		elif mathsymbol == "×":
			result = num1 * num2
			print(result)
			
		elif mathsymbol == "÷":
			result = num1 / num2
			print(result)
			
		elif mathsymbol == "-":
			result = num1 - num2
			print(result)
		else:
			print("Invalid input detected")
	
	print("Utilities Menu:\n1 = Calculator")
	userInput = input("Press 1 for Calculator\n")
	if userInput == "1":
		mathNumbers()
		