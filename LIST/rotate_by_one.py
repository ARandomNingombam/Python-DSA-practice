

ar = list(map(int,input("Enter the numbers: ").split()))

for i in range(len(ar)):
    j = ((i+1) % len(ar))
    temp = ar[j]
    ar[j] = ar[0]
    ar[0] = temp


print(ar)
    

