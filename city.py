from api import Api

class City:
    def __init__(self, name=None):
        self.name = name
        api = Api()
        data = api.fillCity(name)
        if data == None:
            print("Invalid input")
        city_info = data['location_suggestions'][0]

        self.name = city_info["name"]
        self.id = city_info["id"]

    def getCityId(self):
        return self.id
    def getCityName(self):
        return self.name
