print("CALCULATOR")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = (a+b)
print(c)
def add():
	print(a + b)
def subtraction():
	print(a - b)
def multiplication():
	print(a * b)
def divide():
	print(a/b)
f = input("Function: ")
if f == "+":
    add()
elif f == "-":
    subtraction()
elif f == "*":
    multiplication()
elif f =="/":
   #divide()
    if b == 0:
        print("Error: b cannot be 0")
    else:
        divide()
else:
 print("*******")