operator = input("Enter the operator (+ - * /) : ")
num1 = float(input("enter the number 1 : "))
num2 = float(input("enter the number 2 : "))

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
    print(f"{operator} is not found")   





