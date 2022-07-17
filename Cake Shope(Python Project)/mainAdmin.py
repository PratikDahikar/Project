from cakeMng import CakeMng
from cake import Cake

def adminMenuMng():
    cakeMng = CakeMng()
    ch = 0
    while(ch != 10):
        print('''
            1. Add Cake
            2. Search Cake by Name
            3. Search Cake by Id
            4. Edit Cake
            5. Delete Cake
            6. View Cake
            10. Exit
        ''')

        ch = int(input("Enter your choice : "))
        if ch == 1:
            id = int(input("Enter ID : "))
            nm = input("Enter Name : ")
            price = int(input("Enter Price : "))
            qty = int(input("Enter Quantity : "))
            ck = Cake(id,nm,price,qty)
            cakeMng.addCake(ck)

        elif ch == 2:
            nm = input("Enter Cake Name : ")
            cakeMng.searchByName(nm)
            
        elif ch == 3:
            id = input("Enter the id : ")
            cakeMng.searchById(id)

        elif ch == 4:
            id = input("Enter the id : ")
            cakeMng.editById(id)

        elif ch == 5:
            id = input("Enter the id : ")
            cakeMng.deleteById(id)

        elif ch == 6:
            cakeMng.viewCake()

        else:
            pass

if __name__ == "__main__":
    adminMenuMng()