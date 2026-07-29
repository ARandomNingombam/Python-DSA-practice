ar = list(map(int,input("Enter the numbers: ").split()))

even_count=0
odd_count=0

for i in range(len(ar)):
    if(ar[i] % 2 == 0):
        even_count+=1
    else:
        odd_count+=1

print(f"The number of even number is ", even_count," and the number of odd numbers is ",odd_count)