def calculate(num1, op, num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        result = num1 / num2
    elif op == "*":
        result = num1 * num2
    elif op == "%":
        result = num1 % num2
    return result

num1 = int(input("Enter the Number1: "))
op = input("Enter the operator (+, -, /, *, %): ")
num2 = int(input("Enter the Number2: "))

print(num1, op, num2)
result = calculate(num1, op, num2)
print("=", result)
