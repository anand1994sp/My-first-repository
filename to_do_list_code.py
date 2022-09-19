def To_Do_List(n):
    for i in range(1,n+1):
        a=input("TASK"+str(i) + " :")
        list.append(a)
        i += 1
    print("To DO List are :" + str(list))
list=[]
n = int(input("Enter the number of tasks: "))
To_Do_List(n)
