

ar = list(map(int,input("Enter the numbers: ").split()))

ar_0 = []
n = len(ar)
for i in range(n):
    if ar[i] == 0:
        ar_0.append(i)
        ar.append(int(0))

for i in range(len(ar_0)):
    ar.pop(ar_0[i])

print(ar)