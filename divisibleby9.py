# Loop through numbers from 100 to 999
for num in range(100, 1000):
    # Extract digits
    digits_sum = sum(int(digit) for digit in str(num))
    
    # Check if sum of digits is divisible by 9
    if digits_sum % 9 == 0:
        print(num, end=" ")
