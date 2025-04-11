n=int(input("Enter the Limit:\t"))
even_count=0
odd_count=0
for _ in range(n):
    num=int(input("Enter the Numbers\t"))
    if(num%2==0):
        even_count+=1
    else:
        odd_count+=1

print("Even Numbers:",even_count)
print("Odd Numbers",odd_count)
