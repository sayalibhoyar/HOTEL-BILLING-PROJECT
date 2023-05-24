dn={1:"tea",2:"Idli",3:"Dosa",4:"Paratha",5:"Poha",6:"Coffee",7:"Samosa",8:"Uttapa"}
dp={1:12,2:30,3:40,4:50,5:25,6:40,7:30,8:25}
l=[]
q=[]
print("*"*82)
print("\t\t\t\tMAHALAXMI CAFE")
while True:
    print("*"*82)
    print("""
                1.Tea       2.Idli
                3.Dosa      4.Paratha
                5.Poha      6.Coffee
                7.Samosa    8.Uttapa
    """)
    print("-"*82)
    item=int(input("Enter item number:=> "))
    l.append(item)
    quantity=int(input("quantity:=> "))
    q.append(quantity)
    ch=input("Do You want to oder another item(y/n):=> ")
    if ch=="n":
        print("-"*82)
        print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("Sr.no","Item_Name","Quantity","Rate","Amount"))              
        sum=0
        for i in range(len(l)):  
            print("-"*82)
            print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(i+1,dn[l[i]],q[i],dp[l[i]],q[i]*dp[l[i]]))
            print("-"*82)
            sum=sum+q[i]*dp[l[i]]
        print("\t\t\tTotal Amount is to be paid:=> ",sum)
        print("Thank you visit again:)")
        print("*"*82)
        break
                    