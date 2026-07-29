

ar=list(map(int,input("Enter the numbers: ").split()))

max=ar[0]
second_max=ar[0]
for i in ar:
    if(max < i):
        max=i
    if(i<max and i>second_max):
        second_max=i

print(f"The second largest number is ", second_max)
