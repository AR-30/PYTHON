### DIAMOND PATTERN:    
   *
  ***
 *****
  ***
   *  ###
n=int(input("Enter max no. of stars : "))
s=n//2
i=1
while(i<=n):
    for j in range(s):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
    i=i+2
    s=s-1
i=n-2
s=1
while(i>=1):
    for j in range(s):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
    i=i-2
    s=s+1
