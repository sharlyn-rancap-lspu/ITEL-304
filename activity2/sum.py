
#Python program  to add two numbers.

def add(num1, num2):
    sum = num1 + num2
    return sum

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

z = add(x, y)
print(x, "+", y, "=", z)

