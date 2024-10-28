class Rock(object):
    name = ""
    seaLevel = 0
    continent = ""
    country = ""
    
    def __init__(self, name, seaLevel, continent, country):
        self.name = str(name)
        self.seaLevel = float(seaLevel)
        self.continent = str(continent)
        self.country = str(country)
    
    def __str__(self):
        s = ""
        s += str(self.name) + ", "
        s += str(self.seaLevel) + ", "
        s += str(self.continent) + ", "
        s += str(self.country)
        return s
        
        
    def setSeaLevel(self, seaLevel):
        self.seaLevel = seaLevel

def printList(list):
    for r in list:
        print(str(r))

print("Creating list:")
rockList = [
    Rock("Hora1", 1500, "Europe", "Ukraine"),
    Rock("Hora3", 500, "NA", "USA"),
    Rock("Hora2", 2500, "Asia", "Korea")
]
printList(rockList)
print("\n")

print("Adding to list:")
rockList.append(Rock("Hora4", 750, "Australia", "Australia"))
printList(rockList)
print("\n")

print("Removing from list:")
rockList.remove(rockList[0])
printList(rockList)
print("\n")

print("Sorting list by name:")
rockList = sorted(rockList, key= lambda r: r.name)
printList(rockList)
print("\n")
