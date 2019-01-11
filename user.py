class User:

    def __init__(self, userName, password, city):
        self.user_name = userName
        self.passWord = password
        self.city = city

    def addRestaurant(self, restaurant_id):
        if restaurant_name in self.data:
            temp = self.data[restaurant_id]
            self.data[restaurant_id] = temp + 1
        else:
            self.data[restaurant_id] = 1

    def getCount(self, restaurant_id):
        return self.data[restaurant_id]


    #restaurant count and existance is stored in the dictionary data,
    #with the restaurant ID being the key and the count being the value
    def getData(self):
        return self.data
    def set_Data(self, data):
        self.data = data
    def getCity(self):
        return self.city
