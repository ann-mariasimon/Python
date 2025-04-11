import math 

n = int(input('Enter the value of n :'))   # Number of terms
x = float(input('Enter the degree :'))     # Angle in degrees

d = x                    # Store original angle for display
x = math.radians(x)      # Convert degrees to radians

s = 1                    # Initialize sum with first term of series (1)
t = 1                    # Initialize the first term of the series
i = 1                    # Term counter (starting from 1 since 0th term already added)

for i in range(1, n): 
    t = ((-t * x * x)/((2*i)*(2*i - 1)))   # Compute next term using previous term
    s = s + t                              # Add current term to sum

print('cos(', d, ') = %0.2f' % s)
