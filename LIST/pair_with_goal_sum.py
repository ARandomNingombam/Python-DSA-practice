

a = list(map(int,input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))
sum_pair = []

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]+a[j] == target and (a[i],a[j]) not in sum_pair:
            sum_pair.append([a[i],a[j]])

print("The pairs are: ",sum_pair)       