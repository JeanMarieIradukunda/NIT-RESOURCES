# Record calculation Details
num1 = int(input("Enter First Number: "))
operator = input("Enter operator: ")
num2 = int(input("Enter Second Number: "))

# Perform recorded operation
if operator == "+":
    result = num1 + num2
    print("Result: ", result)
elif operator == "-":
    result = num1 - num2
    print("Result: ", result)
elif operator == "*":
    result = num1 * num2
    print("Result: ", result)
elif operator == "/":
    result = num1 / num2
    print("Result: ", result)
else:
    print("Invalid Operator")

