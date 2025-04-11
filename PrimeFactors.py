# Input from user
num = int(input("Enter a number: "))

# Start dividing from 2 (the smallest prime number)
i = 2
print("Prime factors of", num, "are:")

while i <= num:
    if num % i == 0:
        print(i, end=" ")
        num = num // i  # Divide the number and continue with the same i
    else:
        i += 1  # Try the next number
