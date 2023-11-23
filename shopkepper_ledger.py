##SHOPKEEPER LEDGER

import sys

name=[]
quantity=[]
unit_price=[]
while(True):
    c=int(input("Choose operation:\n1:Stock inventory\n2:Buy\n3:Sell\n4:Search\n5:Exit "))
    if(c==1):
        if len(name)==0:
            print("Stock is empty.")
        for i in range(len(name)):
            print(f"{name[i]} : {quantity[i]} : {unit_price[i]}")
    elif(c==2):
        n=input("Enter goods name ")
        q=int(input("Enter quantity "))
        if n in name:
            i=name.index(n)
            quantity[i]=quantity[i]+q
            continue
        t=int(input("Enter unit price "))
        name.append(n)
        quantity.append(q)
        unit_price.append(t)
    elif(c==3):
        n=input("Enter goods name ")
        if n in name:
            i=name.index(n)
            q=int(input("Enter quantity "))
            if  q>quantity[i]:
                print("Insufficient stock")
            else:
                quantity[i]=quantity[i]-q
    elif(c==4):
        n=input("Enter goods name ")
        if n in name:
            i=name.index(n)
            print(f"{n} : {quantity[i]} : {unit_price[i]}")
        else:
            print("Not found.")
    elif(c==5):
        print("Program terminated.")
        sys.exit()
