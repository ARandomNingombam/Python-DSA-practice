
ar = list(map(int,input("Enter the numbers: ").split()))

ele_freq=[]
ele=int([])

for i in ar:
    if i not in ele:
        ele.append([i,0])
    for a,b in enumerate(ele):
        if b == i: 
            ele[a,1]+=1

print(ele)
