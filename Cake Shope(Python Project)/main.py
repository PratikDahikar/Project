from mainAdmin import adminMenuMng
from mainUser import userMenuMng 

ch = int(input('''
        1.Admin
        2.user
    :--> '''))

if ch == 1:
    print("defult id : Admin and password : Admin123")
    id = input("Enter the Username : ")
    psd = input("Enter the Password : ")
    if id == "Admin" and psd == "Admin123":
       adminMenuMng()
    else:
        print("Invalid Credientials..")

elif ch == 2:
    print("defult id : NewUser and password : user123")
    id = input("Enter the username : ")
    psd = input("enter the password : ")
    if id == "NewUser" and psd == "user123":
       userMenuMng()
    else:
        print("Invalid Credientials..")
        
else:
    print("Invalid choice.....")