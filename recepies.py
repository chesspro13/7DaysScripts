class recepie():
    def __init__(self, name):
        self.name = name
        self.ingrediants = []

    def addIngrediant( self, name, amount):
        self.ingrediants.append([name, amount])

    def getIngrediants(self):
        return self.ingrediants

    def saveRecepie(self):
        import json 

        data = []

        recepieFile = "7DTD/recepies.json"
        try:
            f = open( recepieFile, "r")
            data = json.loads(f.read())
            f.close()
            print("First file closed")
        except:
            print("File empty. Creating")

        print("starting data")
        data.append([self.name, None, None])
        print("Preparing data")
        for i in self.ingrediants:
            print("Adding ingrediant")
            data[len(data)-1] = [None, None]
            data[len(data)-1][0] = i[0]
            data[len(data)-1][1] = i[1]
            print("ingrediant added")
        data = json.dumps( data )
        print("Got data")
        f = open( recepieFile, "w")
        f.write( data )
        f.close()
