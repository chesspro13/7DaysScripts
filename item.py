class item():

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        self.have = 0

    def addHave(self, quantity):
        self.have += int(quantity)
        print("You collected more")

    def addNeed(self, quantity):
        self.quantity += int(quantity)


    def getData(self):
        try:
            if( int(self.quantity) - int(self.have) < 0 ):
                print( "\t" + self.name + ": 0" )
            else:
                print( "\t" + self.name + ": " + str(int(self.quantity) - int(self.have)))
        except:
            print("Error getting data")

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity

    def getHave(self):
        return self.have
