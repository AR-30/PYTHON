### counting the number of occurence

l=[1,2,2,2]
d={}
for i in l:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)

