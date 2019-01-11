class Cuisine:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def getCuisineName(self):
        return self.name
    def getCuisineId(self):
        return self.id
    def toString(self):
        return self.name + " has an id of " + str(self.id)


def parseCuisines(lines):
    Cuisines = []
    for cuisine in lines:
        cuisineData = cuisine["cuisine"]
        currentcuisineName = cuisineData["cuisine_name"]
        currentcuisineId = cuisineData["cuisine_id"]
        c = Cuisine(currentcuisineName, currentcuisineId)
        Cuisines.append(c)
    return Cuisines
