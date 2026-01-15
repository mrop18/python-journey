def calculate (num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by 0"
    elif operator == "*":
        return num1 * num2
    else:
        return "Invalid operator"

while True:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+ , - , / , *) : ")
    num2 = float(input("Enter second number: "))

    result = calculate(num1, operator, num2)
    print("Result = ", result)

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == "n":
        print("Calculator closed.")
        break