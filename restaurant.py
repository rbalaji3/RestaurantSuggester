from city import City
from api import Api


class Restaurant:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        api = Api()
        data = api.fillRestaurant(self.name, self.city)
        if data == None:
            print("Invalid input")
            return
        try:
            restaurant_info = data["restaurants"][0]["restaurant"]
            self.name = restaurant_info["name"]
            self.id = restaurant_info["id"]
            self.url = restaurant_info["url"]
            self.location = restaurant_info["location"]
            self.cuisines = restaurant_info["cuisines"]
        except:
            pass
    def getRestaurantId(self):
        return self.id
    def getRestaurantName(self):
        return self.name
    def getRestaurantUrl(self):
        return self.url
    def getRestaurantLocation(self):
        return self.location
    def getRestaurantCuisines(self):
        return self.cuisines
    def to_String(self):
        pass
