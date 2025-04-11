# Input the three sides
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

# Sort the sides to identify the largest (hypotenuse)
sides = sorted([a, b, c])

# Apply Pythagorean theorem directly
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is NOT a right-angled triangle.")
