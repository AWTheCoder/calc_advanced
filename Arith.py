# Subprograms (functions)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Main program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("+  -  *  /")

choice = input("Enter operation: ")

if choice == "+":
    print("Result:", add(num1, num2))

elif choice == "-":
    print("Result:", subtract(num1, num2))

elif choice == "*":
    print("Result:", multiply(num1, num2))

elif choice == "/":
    print("Result:", divide(num1, num2))

else:
    print("Invalid operation")

def perimeter():
    return (2*width) + (2*length)
print("""========================
╔═╗┌─┐┬─┐┬┌┬┐┌─┐┌┬┐┌─┐┬─┐
╠═╝├┤ ├┬┘││││├┤  │ ├┤ ├┬┘
╩  └─┘┴└─┴┴ ┴└─┘ ┴ └─┘┴└─
========================""")
while True:
    try:
        width = float(input("Enter the width of your rectangle/square: "))
        length = float(input("Enter the length of your rectangle/square: "))
        if width < 1 or length < 1:
            print("Must be positive")
            continue
        peri = perimeter()
        print("The perimeter is", peri, "\n")
        break
    except ValueError:
        print("Enter a valid number")
        continue
def area_and_circumference(diameter):
    radius = diameter / 2
    circumference = diameter * 3.14
    area_calc = (radius * radius * 3.14)
    return area_calc, circumference
print("""=============================================================
┌─┐┬─┐┌─┐┌─┐  ┌─┐┌┐┌┌┬┐  ┌─┐┬┬─┐┌─┐┬ ┬┌┬┐┌─┐┌─┐┬─┐┌─┐┌┐┌┌─┐┌─┐
├─┤├┬┘├┤ ├─┤  ├─┤│││ ││  │  │├┬┘│  │ ││││├┤ ├┤ ├┬┘├┤ ││││  ├┤ 
┴ ┴┴└─└─┘┴ ┴  ┴ ┴┘└┘─┴┘  └─┘┴┴└─└─┘└─┘┴ ┴└  └─┘┴└─└─┘┘└┘└─┘└─┘
=============================================================""")
while True:
    try:
        diameter = float(input("Enter the diameter of the circle: "))
        if diameter <= 0:
            print("Must be positive")
            continue
        area_calc, circ_calc = area_and_circumference(diameter)
        print("The area of your circle is", area_calc)
        print("The circumference of your circle is", circ_calc)
        break
    except ValueError:
        print("Enter a valid number")
        continue
