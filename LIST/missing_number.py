


ar =  list(map(int,input("Enter the numbers: ").split()))

ar.sort()

a = 0
b = len(ar)

while a<=b:
    mid = (a+b)//2
    if ar[mid] == mid + 1:
        a = mid + 1
    else:
        b = mid -  1

if ar[a] != a+1:
    print(f"Missing numnber is: ",a+1)
else:
    print("No missing number!")