class main():

    def saveData(self):
        import json
        fileDir = "7DTD/list.json"
        f = open( fileDir, "w")
        itemData = []
        for i in self.items:
            itemData.append([i.getName(), i.getQuantity(), i.getHave()])
        writeData = [itemData, self.tasks]
        data = json.dumps( writeData )
        f.write(data)
        f.close()

    def loadData(self):
        import json
        fileDir = "7DTD/list.json"
        f = open( fileDir, 'r')
        data = f.read()
        data = json.loads(data)
        for i in data[0]:
            self.insertItem(i[0], i[1], i[2])
#       self.items = data[0]
        self.tasks = data[1]

    def insertItem(self, name, amount, have):
        found = False
        for i in self.items:
            if i.getName().lower() == name.lower():
                found = True
                i.addNeed( amount )

        if found == False:
            self.items.append(item(name, amount))

    def addItem(self):
        name = input("What item do you need to gather?\n>")
        amount = input("How many do you need?\n>")
        found = False
        for i in self.items:
            if i.getName().lower() == name.lower():
                print("Adding to existing item!")
                found = True
                i.addNeed( amount )

        if found == False:
            self.items.append(item(name, amount))
        print("item added")

    def __init__(self):
        from need import item
        import json
        import os

        print("Starting the resource tracker")
        self.items = []
        self.tasks = []



        while True:
            os.system("clear")


            print("Items tracking:")
            for i in self.tasks:
                print( "\t" + i )
            print("Resources Tracking:")
            for i in self.items:
                i.getData()
            print("\n\n")
            try: 
                result = self.getInput('What do you want to do?', ["Add item", "Remove item", "Increase needed", "Add items to item", "Add tracked item", "Remove tracked item", "Save list", "Load list", "Add recepie", "Create recepie"])
                if result == "0":
                    self.addItem()
                elif result == "1":
                    result = self.getInput('What do you want to remove from the list? ', self.items)
                    self.items.remove(i)
                elif result == "2":
                    item = self.getInput("What item do you want to add to?", self.items)
                    result = input("How many do you want to add?\n>")
                    try:
                        self.items[int(item)].addNeed(int(result))
                        print("Adding items to " + self.items[int(item)].getName())
                    except:
                        print("Error")
                elif result == "3":
                    item = self.getInput("What item do you want to add to?", self.items)
                    result = input("How many do you want to add?\n>")
                    try:
                        self.items[int(item)].addHave(int(result))
                    except:
                        print("Error")
                elif result == "4":
                    result = input("What item are you crafting?\n>")
                    self.tasks.append( result )
                elif result == "5":
                    result = self.getInput('Which task do you want to remove from the list?', self.tasks)
                    print( result )
                    print( self.tasks )
                    self.tasks.remove( self.tasks[int(result )])
                elif result == "6":
                    self.saveData()
                elif result == "7":
                    self.loadData()
                elif result == "8":
                    print("TODO: ")
                elif result == "9":
                    self.createRecepie()
            except Exception as e:
                 print("Error")
                 print( e )
                 input()

    def createRecepie(self):
        from need import recepie


        name = input("What recepie are you creating?\n>")
        r = recepie( name)

        ingrediantCount = input("How many ingrediants are in this recipie?\n>")

        
        for i in range( int(ingrediantCount) ):
            result = input("What is the " + self.tense(str(i)) + " resource in this recipie?\n>")
            count = input('How many "' + result + '" do you need?\n>')

            r.addIngrediant( result, int( count ))
            
        r.saveRecepie()


    def tense(self, num):
        if num == "0":
            return "1st"
        elif num == "1":
            return "2nd"
        elif num == "2":
            return "3rd"
        elif num == "3":
            return "4th"
        elif num == "4":
            return "5th"


    def getInput(self, prompt, options):
        print( prompt )
        count = 0
        try:
            for i in options:
                print( str(count) + ": " + str(i.getName() ))
                count += 1
        except:
            for i in options:
                print( str(count) + ": " + str(i))
                count += 1

        return input()
