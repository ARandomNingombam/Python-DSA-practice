
ar = list(map(int,input("Enter the numbers: ").split()))
rev_dupli = []

for i in range(len(ar)):
    if ar[i] not in rev_dupli:
        rev_dupli.append(ar[i])

print(f"Duplicates Removed!: ", rev_dupli)