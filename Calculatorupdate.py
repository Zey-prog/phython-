print ("Calculator\n")

a = input("Enter first number: ")
num1 = int(a)
op = input("Enter operation: ")
b = input("Enter second number: ")
num2 = int(b)


if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else :
    print ("You enter a operator!")
    
print( a, op, b,"=", result)