

class Cake:
    def __init__(self,id = 111,name = "newCake",price = 300,qty = 10):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def __str__(self):
        data = str(self.id) + "," + self.name + "," + str(self.price) + "," + str(self.qty)
        return data

if __name__ == "__main__":
    ck = Cake(111,"mango",250)
    print(ck)