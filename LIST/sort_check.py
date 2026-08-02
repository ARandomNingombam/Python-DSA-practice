

ar = list(map(int,input("Enter the numbers: ").split()))

for i in range(len(ar)-1):
    flag = False
    if ar[i] > ar[i+1]:
        flag = True
        break

if flag: 
    print("The list is not sorted")
else: 
    print("The list is sorted")

