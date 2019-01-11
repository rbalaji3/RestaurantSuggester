import requests
class Api:
    def __init__(self):
        self.apiKey = "13e1585c0eb9d8d7b3b67bd6baebc759"
        self.header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": self.apiKey}


    def fillCity(self, city_name):
        searchURL = "https://developers.zomato.com/api/v2.1/cities?q=" + str(city_name)
        searchresponse = requests.post(searchURL, headers=self.header)
        if searchresponse == 403:
            return None
        data = searchresponse.json()
        return data

    def fillCuisine(self, cuisine_name, city):
        searchURL = "https://developers.zomato.com/api/v2.1/cuisines?city_id=" + str(city.getCityId())
        searchresponse = requests.post(searchURL, headers=self.header)
        if searchresponse == 403:
            return None
        data = searchresponse.json()
        return data["cuisines"]


    def fillRestaurant(self, name, city):
        searchURL = "https://developers.zomato.com/api/v2.1/search?entity_id=" + str(city.getCityId()) + "&entity_type=city&q=" + str(name)
        searchresponse = requests.post(searchURL, headers=self.header)
        if searchresponse == 403:
            return None
        data = searchresponse.json()
        return data
    def getRestaurant(self, res_id):
        searchURL = "https://developers.zomato.com/api/v2.1/restaurant?res_id=" + res_id
        searchresponse = requests.post(searchURL, headers=self.header)
        if searchresponse == 403:
            return None

        data = searchresponse.json()
        return data["name"]

    def getAllCuisines(self, city):
        searchURL = "https://developers.zomato.com/api/v2.1/cuisines?city_id=" + str(city.getCityId())
        searchresponse = requests.post(searchURL, headers=self.header)
        if searchresponse == 403:
            return None

        data = searchresponse.json()
        cuisine_name_list = []
        for ele in data["cuisines"]:
            cuisine_name_list.append(ele["cuisine"]["cuisine_name"])
        return cuisine_name_list

    def getRestaurantsgivenCuisine(self, city, cuisine): # returns a list of restaurants in a given a city that serve given cuisine
        searchURL = "https://developers.zomato.com/api/v2.1/search?entity_id=" + str(city.getCityId()) + "&entity_type=city&cuisines=" + str(cuisine.getCuisineId())
        searchresponse = requests.post(searchURL, headers=self.header)
        if searchresponse == 403:
            return None
        data = searchresponse.json()
        return data






#
# cityURL = "https://developers.zomato.com/api/v2.1/cities?q=" + city
# cityresponse = requests.post(cityURL, headers=header)
#
# City = City(cityresponse.json())
# print(City.getCityId())
# #
# # cuisineURL = "https://developers.zomato.com/api/v2.1/cuisines?city_id=" + str(City.getCityId())
# # print("Cityid of ", city ,City.getCityId())
# # cuisineresponse = requests.post(cuisineURL, headers=header)
#
# # lines = cuisineresponse.json()["cuisines"]
# # #print(lines)
# # CuisineList = []
# # CuisineList = parseCuisines(lines)
# # for c in CuisineList:
# #     print(c.getCuisineName())
# #     Cuisine = c
#
# restaurantURL = "https://developers.zomato.com/api/v2.1/search?entity_id=" + str(City.getCityId()) + "&entity_type=city&cuisines=" + str(148)
# restaurantResponse = requests.post(restaurantURL, headers=header)
# data = restaurantResponse.json()
# for key in data["restaurants"]:
#     print(key["restaurant"]["name"])
