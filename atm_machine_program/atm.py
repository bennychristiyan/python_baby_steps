print("welcome to sbi")
while (True):
    print("plz enter the language:")
    print("1.english")
    print("2.tamil")
    print("3.hindi")
    print("4.japanese")
    aa = 99999999
    a = int(input())
    if a==1:
        print("enter an option:")
        print("1.deposit")
        print("2.withdraings")
        print("3.current")
        print("4.mini statement")
        b = int(input())
        if b==1:
            c = int(input("enter the pin:"))
            d = int(input("enter the amount:"))
            f = aa+d
            print("your current balance is ",f)
            print("do u need the receipt or not:")
            print("1.no")
            print("2.yes")
            e = int(input("plz choose the option "))
            if e==1:
                print("thank you for coming")
            elif e==2:
                print("plz collect the receipt")
                print("thank you for coming")
            else:
                print("invalid option, insert the card again")
            break
        elif b==2:
            c = int(input("enter the pin:"))
            d = int(input("enter the amount:"))
            f = aa-d
            print("your current balance is ",f)
            print("do u need the receipt or not:")
            print("1.no")
            print("2.yes")
            e = int(input("plz choose the option "))
            if e==1:
                print("thank you for coming")
            elif e==2:
                print("plz collect the receipt")
                print("thank you for coming")
            else:
                print("invalid option, insert the card again")
            break    
        elif b==3:
            c = int(input("enter the pin:"))
            print("your current balance is ",aa)
            print("do u need the receipt or not")
            print("1.no")
            print("2.yes")
            e = int(input("plz choose the option "))
            if e==1:
                print("thank you for coming")
            elif e==2:
                print("plz collect the receipt")
                print("thank you for coming")
            else:
                print("invalid option, insert card again")
            break
        elif b==4:
            c = int(input("enter the pin:"))
            print("plz collect the receipt")
            print("thank you for coming")
            break
        else:
            print("invalid option, insert the card again")
            break
    elif a ==2:
        print("plz choose english, tamil is unavailable right now")
    elif a==3:
        print("plz choose english, hindi is unavailable right now")
    elif a==4:
        print("plz choose english, japanese is unavailable right now")
    else:
        print("invalid option")    
        