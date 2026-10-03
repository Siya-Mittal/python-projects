# Python calculator
operator = input("Enter an operator(+ * * /): ")
num1 = float(input("Enter the first no :"))
num2 = float(input("Enter the second no :"))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator")
