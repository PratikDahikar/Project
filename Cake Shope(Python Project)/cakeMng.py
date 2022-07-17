from os import path
from cake import Cake

class CakeMng:
    def addCake(self,ck):
        with open("cakeInfo.txt","a") as fp:
            fp.write(str(ck))
            fp.write("\n")

    def searchByName(self,nm):
        if(path.exists("cakeInfo.txt")):
            with open("cakeInfo.txt", "r") as fp:
                for line in fp:
                    if nm in line:
                        data = line.split(",")
                        print(f"ID : {data[0]} \nName : {data[1]} \nPrice : {data[2]} \nQuantity : {data[3]}")
                        break
                else:
                    print("Cake is not Avilable.....")    
        else:
            print("file not found......")

    def searchById(self,id):
        if(path.exists("cakeInfo.txt")):
            with open("cakeInfo.txt", "r") as fp:
                flag = False
                for line in fp:
                    data = line.split(",")
                    if data[0] == id:
                        print(f"ID : {data[0]} \nName : {data[1]} \nPrice : {data[2]} \nQuantity : {data[3]}")
                        flag = True
                        break
            if flag == False:
                print("Cake is not Avilable......")
        else:
            print("file not found....")

    def belowPrice(self,pr):
        if(path.exists("cakeInfo.txt")):
            with open("cakeInfo.txt", "r") as fp:
                flag = False
                for line in fp:
                    data = line.split(",")
                    dataPr = int(data[2])
                    if dataPr <= pr:
                        print(line.strip())
                        flag = True
            if flag == False:
                print("There is no cake Below ",pr)
        else:
            print("file not found....")
    
    def editById(self,id):
        cakeList =[]
        flag = False
        if(path.exists("cakeInfo.txt")):
            with open("cakeInfo.txt", "r") as fp:
                for line in fp:
                    data = line.split(",")
                    if data[0] == str(id):
                        flag = True
                        print("Cake is Avilable....\n",line.strip())

                        ans = input("Do you wish to change Cake name (y/n) : ")
                        if ans.lower() == "y":
                            data[1] = input("Enter Cake Name : ")

                        ans = input("Do you wish to change Cake Price (y/n) : ")
                        if ans.lower() == "y":
                            data[2] = input("Enter Cake Price : ")

                        ans = input("Do you wish to change Cake Quantity (y/n) : ")
                        if ans.lower() == "y":
                            data[3] = input("Enter Cake Quantity : ")
                        line = ",".join(data)
                        line += "\n"
                        print("hello-1")
                    cakeList.append(line)
                    print("hello-2")
            if flag == True:
                with open("cakeInfo.txt", "w") as fp:
                    for ck in cakeList:
                        fp.write(ck)
                    print("Details updated...")
            else:
                print(f"There is no cake with ID : {id}")               
        else:
            print("file not found")

    def deleteById(self,id):
        cakeList = []
        flag = False
        if path.exists("cakeInfo.txt"):
            with open("cakeInfo.txt", "r") as fp:
                for line in fp:
                    data = line.split(",")
                    if data[0] == str(id):
                        flag = True
                    else:
                        cakeList.append(line)
            if flag == True:
                with open("cakeInfo.txt", "w") as fp:
                    for ck in cakeList:
                        fp.write(ck)
            else:
                print("There is no cake with ID : ",id)
        else:
            print("file not found .....")
    
    def viewCake(self):
        if(path.exists("cakeInfo.txt")):
            with open("cakeInfo.txt", "r") as fp:
                print("%6s %12s %6s %4s"%("ID", "Cake Name", "Price", "Qty"))
                print("   ----------------------------")
                for line in fp:
                    data = line.split(",")
                    print("%6s %12s %6s %4s"%(data[0], data[1], data[2], data[3].strip()))
                    # print(data[0])
        else:
            print("file not found....")


        

if __name__ == "__main__":
    # CakeMng.searchByName("mango")
    # CakeMng().searchById("122")
    # CakeMng.belowPrice(22)
    # CakeMng().editById(113)
    # CakeMng().deleteById(116)
    CakeMng().viewCake()