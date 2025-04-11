# Get the lower and upper limits from the user
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

# Initialize sum variable
odd_sum = 0

# Loop through the range and add only odd numbers
for num in range(lower, upper + 1):
    if num % 2 != 0:  # Check if the number is odd
        odd_sum += num

# Display the result
print("Sum of odd numbers between", lower, "and", upper, "is:", odd_sum)
