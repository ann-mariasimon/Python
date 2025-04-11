import cmath 

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = (b ** 2) - (4 * a * c)

root1 = (-b + cmath.sqrt(D)) / (2 * a)
root2 = (-b - cmath.sqrt(D)) / (2 * a)

print("The roots of the equation are:")
print("Root 1 =", root1)
print("Root 2 =", root2)
