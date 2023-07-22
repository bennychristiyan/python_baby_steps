while(True):
    print("STUDENT'S BLOOD INFORMATION")
    print("a.CSE")
    print("b.ECE")
    print("c.MECH")
    print("d.CIVIL")
    print("e.EXIT")
    a = ["person1","A+","yes","person2","B+","no","person3","A+","yes","person4","B+","no","person5","AB+","yes"]
    b = ["person1","B+","no","person2","A+","yes","person3","A+","no","person4","O+","yes","person5","AB+","yes"]
    c = ["person1","AB+","yes","person2","O+","no","person3","A+","yes","person4","A+","no","person5","B+","yes"]
    d = ["person1","O+","yes","person2","AB+","no","person3","O+","no","person4","A+","yes","person5","B+","yes"]
    group = input("enter the department: ")
    if(group!="a" and  group!="b" and  group!="c" and  group!="d" and  group!="e"):
        print("invalid option")
    elif (group=="a"):
        print("STUDENT'S NAME\tBLOOD GROUP\tELIGIBLE OR NOT")
        for i in range(0,15,3):
            print(a[i],"\t\t\t", a[i+1],"\t\t", a[i+2])
    elif (group=="b"):
        print("STUDENT'S NAME\tBLOOD GROUP\tELIGIBLE OR NOT")
        for i in range(0,15,3):
            print(b[i],"\t\t\t", b[i+1],"\t\t", b[i+2])     
    elif (group=="c"):
        print("STUDENT'S NAME\tBLOOD GROUP\tELIGIBLE OR NOT")
        for i in range(0,15,3):
            print(c[i],"\t\t\t", c[i+1],"\t\t", c[i+2])        
    elif (group=="d"):
        print("STUDENT'S NAME\tBLOOD GROUP\tELIGIBLE OR NOT")
        for i in range(0,15,3):
                print(d[i],"\t\t\t", d[i+1],"\t\t", d[i+2])
    elif(group=="e"):
        print("thank you for ur visit")
        break
