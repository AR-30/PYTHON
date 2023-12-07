### printing first n prime numbers
n=int(input("Enter number "))
k=0
j=2
print(f"First {n} prime numbers are:", end=" ")
while(k!=n):
    value=0
    for i in range(2,j):
        if(j%i==0):
            value=1
    if(value==0):
        print(j, end=", ")
        k+=1
    j+=1
