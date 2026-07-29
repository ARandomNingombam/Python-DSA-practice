ar = list(map(int,input("Enter the numbers: ").split()))

sum=0

for i in range(len(ar)):
    sum = sum + ar[i]

print(f"The sum of all the elements is ", sum)