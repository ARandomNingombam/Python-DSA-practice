
ar = list(map(int,input("Enter the numbers: ").split()))

rev=[]
n = len(ar)

for i in range(n):
    rev.append(ar[n-i-1])

print(f"The reversed list is ", rev)