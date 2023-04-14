print("CALCULATOR\n")

a = input("")
a1 = int(a)
b = input("")
c = input("")
c1 = int(c)


if b == "+":
    result = a1 + c1
    print("=", result)

elif b == "-":
    result = a1 - c1
    print("=", result)

elif b == "/":
    result = a1 / c1
    print("=", result)

elif b == "x":
    result = a1 * c1
    print("=", result)

print("Type \"clear\" to delete all numbers\n")

d = input(":")

#if d == "clear":
