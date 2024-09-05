# finding sq of a number list in different ways

#simple for loop
l=[1,2,3,4,5]
nl=[]
for i in l:
  nl.append(i*i)
print(nl)

#list comprehension
l=[1,2,3,4,5]
print([i*i for i in l])

#function with for loop
def sq(x):
  return x*x
  
l=[1,2,3,4,5]
nl=[]
for i in l:
  nl.append(sq(i))
print(nl)

#defining the function and map function
def sq(x):
  return x*x

l=[1,2,3,4,5]
print(list(map(sq,l)))

#lambda function : implicit function defining
l=[1,2,3,4,5]
print(list(map(lambda x:x**2, l)))
