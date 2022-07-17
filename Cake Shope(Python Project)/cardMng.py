from os import path

def addToCard(id):
    cakeList = []
    cardList = []
    flag = False
    flag2 = True
    if(path.exists("cakeInfo.txt")):
        with open("cakeInfo.txt", "r") as fp:
            for line in fp:
                data = line.split(",")
                if id.isdigit():
                    i = 0
                else: 
                    i = 1
                if data[i] == id:
                    flag2 = False
                    print(f"{data[1]} cake is avilable....\nPrice : {data[2]} \nQuantity : {data[3]}")
                    qty = int(input(f"how many {data[1]} cake you want : "))
                    avilableQty = int(data[3]) 
                    if qty <= avilableQty:
                        data[3] = str(avilableQty - qty)
                        flag = True
                    else:
                        print(f"Enter the quantity less than the avilable...")
                        break
                    line = ",".join(data)
                    line += "\n"
                    print(line)
                    cardList.append(data[1])
                    cardList.append(data[2])
                    cardList.append(str(qty))
                    cardItem = ",".join(cardList)
                    print(cardItem)
                    cardItem += "\n"
                cakeList.append(line)    
        if flag == True:        
            with open("cakeInfo.txt", "w") as fp:
                for ck in cakeList:
                    fp.write(ck)
            
            with open("cardInfo.txt", "a") as fp:               
                fp.write(cardItem)
                print("Cake successfully added to your card")
        if flag2 == True:
            print("cake not found")
    else:
        print("file not found")

def removeFromCard(nm):
        cardList = []
        flag = False
        qty = 0
        if path.exists("cardInfo.txt"):
            with open("cardInfo.txt", "r") as fp:
                for line in fp:
                    data = line.split(",")
                    if data[0] == nm:
                        qty = int(data[2])
                        flag = True
                    else:
                        cardList.append(line)
            if flag:
                with open("cardInfo.txt", "w") as fp:
                    for ck in cardList:
                        fp.write(ck)
                
                with open("cakeInfo.txt", "r") as fp:
                    cakeList = []
                    for line in fp:
                        data = line.split(",")
                        if data[1] == nm: 
                            qty += int(data[3])
                            data[3] = str(qty)
                            line = ",".join(data)
                            line += "\n"
                        cakeList.append(line)
                with open("cakeInfo.txt", "w") as fp:
                    for ck in cakeList:
                        fp.write(ck)
                                
            else:
                print("invalid Name")
        else:
            print("file not found .....")

def editById(nm):
        cakeList = []
        cardList = []
        flag = False
        if(path.exists("cardInfo.txt")):
            with open("cardInfo.txt", "r") as fp:
                for line in fp:
                    data = line.split(",")
                    if data[0] == nm:
                        # flag = True
                        if(path.exists("cakeInfo.txt")):
                            with open("cakeInfo.txt", "r") as fq:
                                for line2 in fq:
                                    data2 = line2.split(",")
                                    if data2[1] == nm:
                                        qty = int(input("enter the qantity : "))
                                        data[2] = int(data[2])
                                        data2[3] = int(data2[3])
                                        if qty > data[2]:
                                            ext = qty - data[2]
                                            if ext <= data2[3]:
                                                data2[3] -= ext
                                                data[2] = qty
                                                flag = True
                                                print("Change is updated...")
                                            else: 
                                                print(f"extra {ext} cakes are not avilable...")
                                        elif qty < data[2]:
                                            ext = data[2] - qty
                                            data2[3] += ext
                                            data[2] -= ext
                                            flag = True
                                            print("Change is updated...")
                                        data[2] = str(data[2])
                                        data2[3] = str(data2[3])
                                        line = ",".join(data)
                                        line += "\n"
                                        line2 = ",".join(data2)
                                        line2 += "\n"
                                    cakeList.append(line2)
                        else:
                            print("file not exit")
                    cardList.append(line)    
            if flag:
                with open("cakeInfo.txt", "w") as fp:
                    for ck in cakeList:
                        fp.write(ck)

                with open("cardInfo.txt", "w") as fp:
                    for ck in cardList:
                        fp.write(ck)            
        else:
            print("file not found")
 
def viewCake():
        if(path.exists("cardInfo.txt")):
            with open("cardInfo.txt", "r") as fp:
                print("   Cake Name|       Price|    Quantity|")
                for line in fp:
                    data = line.split(",")
                    print("%12s %12s %12s"%(data[0],data[1],data[2]),end = "")
        else:
            print("file not found....")

def placeOrder():
    if(path.exists("cardInfo.txt")):
        with open("cardInfo.txt","r") as fp:
            print("%12s %12s %12s %12s"%("Cake Name|", "Price|", "Quantity|", "Total|"))
            total = 0
            for line in fp:
                data = line.split(",")
                totalCk = int(data[1]) * int(data[2])  
                print("%12s %12s %12s %12d"%(data[0], data[1], data[2].strip(), totalCk))           
                total += totalCk
            print("----------------------------------------------------")
            print("%38s %12d/-"%("Total :", total))

            ch = input(f"Place Order (y/n) : ") 
            if ch == "y" or ch == "Y":
                print("Order Place Succesfully.........")
                with open("cardInfo.txt", "w") as fp:
                    pass
    else: 
        print("File not found.....")

if __name__ =="__main__":
    # id = input("enter the id : ")
    # addToCard(id)
    # nm = input("enter the name : ")
    # editById(nm)
    viewCake()
    # placeOrder()

        

