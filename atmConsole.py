l=[]
balance=1000000
while(True):
    choice=int(input("Choose option:\n1:Deposite\n2:Withdraw\n3:Ministatement\n4:Exit "))
    if(choice==1):
        amt=int(input("Enter amount: "))
        if(amt%100!=0):
            print("Amount cannot be deposited.")
            continue
        else:
            denomination=int(input("Enter denomination: "))
            total_notes=amt/denomination
            if(total_notes>200):
                print("Exceded note limit.")
                continue
            balance=balance+amt
            print(f"{amt} deposited successfully")
            print(f"Balance = {balance}")
            if(len(l)==5):
                del l[0]
            l.append('deposite')
    elif(choice==2):
        w=int(input("Enter amount to be withdrawal"))
        if(w>balance or w%100!=0):
            print("Insufficient balance.")
            continue
        elif(w>10000):
            otp=input("Enter OTP")
            if(len(otp)>4 or len(otp)<4):
                print("Invalid OTP")
                continue
        balance=balance-w
        print(f"{w} deducted from account.")
        print(f"Balance = {balance}")
        if(len(l)==5):
            del l[0]
        l.append("withdraw")
    elif(choice==3):
        print("Ministatement: ")
        print(*l,"\n")
    elif(choice==4):
        print("Program terminated")
        break
    else:
        print("Enter valid choice")

