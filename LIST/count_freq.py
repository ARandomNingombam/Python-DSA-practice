
ar = list(map(int,input("Enter the numbers: ").split()))

freq = []

for i in ar:
    f = False
    for item in freq:
        if item[0] == i:
            item[1] += 1
            f = True
            break

    if not f:
        freq.append([i,1])

print(f"The frequency of the elements are: ", freq)
