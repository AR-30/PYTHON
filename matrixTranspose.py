# transpose of a matrix

n=int(input("Enter matrix size: "))
a=[]
print("Enter matrix elements: ")
for i in range(n):
    m=[]
    for j in range(n):
        m.append(int(input()))
    a.append(m)
print("matrix:")
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
print("transpose: ")
for i in range(n):
    for j in range(n):
        print(a[j][i],end=" ")
    print()
