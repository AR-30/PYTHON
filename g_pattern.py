## pattern 'G'

n = int(input("Enter number of lines "))
for i in range(n):
    for j in range(n):
        if(i==0 and j!=0) or (i==n-1 and j!=0 and j!=n-1):
            print("*", end="")
        elif(i!=0 and i<n//2 and j==0):
            print("*", end="")
        elif(i==n//2 and (j>=n//2 or j==0)):
            print("*", end="")
        elif(i>n//2 and i!=n-1 and (j==0 or j==n-1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
