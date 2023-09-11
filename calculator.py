a = int(input("enter first value:"))
operator = input("enter operator (+,-,*,/,%,//) :")
b = int(input("enter second value:"))
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator == "%":
    print(a % b)
elif operator == "//":
    print(a // b)

else:
    "Invalid value "

