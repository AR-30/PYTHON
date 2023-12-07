### printing first n prime numbers
n=int(input("Enter number "))
i=0
j=2
print(f"First {n} prime numbers are:", end=" ")
while(i!=n):
    value=0
    for k in range(2,j):
        if(j%k==0):
            value=1
    if(value==0):
        print(j, end=", ")
        i+=1
    j+=1
