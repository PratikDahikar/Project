from cakeMng import CakeMng
from cardMng import *

def userMenuMng():
    ch = 0
    while( ch != 10):
        print('''
            1. View Cake
            2. Search Cake by Name
            3. Search Cake by Id
            4. Add to card
            5. Remove from card
            6. Edit
            7. View Card Details
            8. Place order
            10. Exit
        ''')

        ch = int(input("Enter you choise : "))

        if ch == 1:
            CakeMng().viewCake() 

        elif ch == 2:
            nm = input("Enter Cake Name : ")
            CakeMng().searchByName(nm)
            
        elif ch == 3:
            id = input("Enter the id : ")
            CakeMng().searchById(id)

        elif ch == 4:
            id = input("Enter cake (ID/Name) : ")
            addToCard(id)

        elif ch == 5:
            nm = input("Enter cake Name : ")
            removeFromCard(nm)

        elif ch == 6:
            nm = input("Enter cake name : ")
            editById(nm)

        elif ch == 7:
            viewCake()

        elif ch == 8:
            placeOrder()


if __name__ == "__main__":
    userMenuMng()