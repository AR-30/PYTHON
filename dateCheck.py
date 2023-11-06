#check whether the date is valid or not.


d,m,y=map(int,input("Enter the date in format dd/mm/yyyy : ").split('/'))
if(d==0 or d>31 or m==0 or m>12 or y==0):
    print("Invalid date")
else:
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        print("Valid date")
    elif(m==2):
        if(y%4==0):
            if(d<=29):
                print("Valid date")
            else:
                print("Invalid date")
        else:
            if(d<=28):
                print("Valid date")
            else:
                print("Invalid date")
    else:
        if(d<=30):
            print("Valid date")
        else:
            print("Invalid date")
