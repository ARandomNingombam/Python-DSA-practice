

a = list(map(int,input("Enter the numbers for the first: ").split()))
b = list(map(int,input("Enter the numbers for the second: ").split()))

dup = []

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if a[i] not in dup:
                dup.append(a[i])

print("The duplicates are: ", dup)