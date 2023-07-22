print("STUDENT MARK LIST")
aa = input("enter the student name: ")
while(True):
    try:
        bb = int(input("enter roll no.: "))
        break
    except(ValueError):
        print("enter integers only")
while(True):
    try:
        a = int(input("enter the mark of subject 1: "))
        if (a<0 or a>100):
            print("invalid mark")
        else:
            break
    except(ValueError):
        print("enter integers only")
while(True):
    try:
        b = int(input("enter the mark of subject 2: "))
        if (b<0 or b>100):
            print("invalid mark")
        else:
            break
    except(ValueError):
        print("enter integers only")
while(True):
    try:
        c = int(input("enter the mark of subject 3: "))
        if (c<0 or c>100):
            print("invalid mark")
        else:
            break
    except(ValueError):
        print("enter integers only")
while(True):
    try:
        d = int(input("enter the mark of subject 4: "))
        if (d<0 or d>100):
            print("invalid mark")
        else:
            break
    except(ValueError):
        print("enter integers only")
while(True):
    try:
        e = int(input("enter the mark of subject 5: "))
        if (e<0 or e>100):
            print("invalid mark")
        else:
            break
    except(ValueError):
        print("enter integers only")
while(True):
    try:
        f = int(input("enter the mark of subject 6: "))
        if (f<0 or f>100):
            print("invalid mark")
        else:
            break
    except(ValueError):
        print("enter integers only")
        
    
total = a+b+c+d+e+f
percentage = total//6
print("the percentage is ",percentage)
if(a<35 or b<35 or c<35 or d<35 or e<35 or f<35):
    print("Fail")
elif (percentage>90 and percentage<=100):
    print("S grade")
elif (percentage>80 and percentage<=90):
    print("A grade")
elif (percentage>70 and percentage<=80):
    print("B grade")
elif (percentage>60 and percentage<=70):
    print("C grade")
elif (percentage>50 and percentage<=60):
    print("D grade")
elif (percentage>34 and percentage<=50):
    print("E grade")
elif (percentage>=0 and percentage<=34):
    print("Fail")
