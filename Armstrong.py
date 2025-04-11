# Input from user
num = int(input("Enter a number: "))

# Find the number of digits
n = len(str(num))

# Calculate the sum of the nth powers of its digits
sum_of_powers = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** n
    temp //= 10

# Check if the number is an Armstrong number
if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
