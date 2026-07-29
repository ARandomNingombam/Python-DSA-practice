ar = list(map(int,input("Enter the numbers: ").split()))

n=len(ar)

for i in range(int(n/2)):
    temp=ar[n-i-1]
    ar[n-i-1]=ar[i]
    ar[i]=temp

print("The reversed list is ",ar)