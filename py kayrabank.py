import time
employeepasswords=[]
customerpasswords=[]
a= 0 
numberbankaccounts= a
listnumber=0
allaccounts=[]
profileid=[]
allfinished= False
done = False
 
while allfinished is False:
 c=str(input(f"how can I help you\n  customer_service \n  employee services"))
 if c == "customer_service":
    
  
   customerfinished = False
   while customerfinished is False:
    answer=(str(input(" do you want to open a bank account")))
    answer= answer.lower()
    
    
    if answer != "yes":
        useraccess=input("what is the password of your account?")
        while useraccess in customerpasswords:
                e=input("enter profile id")
                for i in range(len(profileid)):
                   if profileid[i]==e:
                       print("access accepted")
                       time.sleep(1)
                
                   else:
                      print("access denied")   
                      customerfinished = True
                 
        else:
               print("access denied")
               customerfinished = True
            
        
    
    elif answer == "yes":
        a = a + 1  
        
        name=str(input("your name"))
        idnumber=float(input("your id number"))
        age=input("your age")
        citizenship=input( "citizenship")
        print(" wait a second")
        time.sleep(3)
        newcustomerpassword=int(input("create a password"))
        customerpasswords.append(newcustomerpassword)
        newprofileid=f"{name}{a}"
        profileid.append(newprofileid)
        print (f"your profile id is {profileid}.")
        e_list  = [["newprofileid"],["newcustomerpassword"]]
                             
 

        newaccount= list[name, idnumber, age, citizenship]
        allaccounts.append(newaccount)
        print(f"this bank has {a} accounts")
        print(f"dear {name}, your account has been created")
        b= input("did you done")
        b= b.lower()
        if b== "yes":
           customerfinished = True
           break
 else:
   d=input("do you have password")
   d=d.lower()
   
   if d== "yes":
       employeepassword=input("enter the password")
       bool(employeepassword)
       if employeepassword == True:
           print("access allowed")
           print(allaccounts and a)
   else:
    
       e=input("do you work in Kayrabank")
       e=e.lower()
       if e=="yes":
           print("fuck you then")
           
       else:
           newpassword=input("enter new password")
           employeepasswords.append(newpassword)
          
 
 

 

    

