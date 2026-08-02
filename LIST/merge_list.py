
a = list(map(int,input("Enter the numbers for the first: ").split()))
b = list(map(int,input("Enter the numbers for the second: ").split()))

for i in b:
    a.append(i)

print(f"The merge list is: ", a)