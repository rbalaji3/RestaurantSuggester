import random
from api import Api
from restaurant import Restaurant
from cuisine import Cuisine
class Suggest:
    def familiar(self, user): # suggest something (RETURNS A RESTAURANT NAME) from the top 25% places the user visits
        data = user.getData()
        len_dict = len(data)
        percentage = int(.25 * len_dict)
        sortvers = sorted(data.items(), key=lambda x: x[1])
        tops = []
        for i in range(len_dict - percentage, len_dict):
            tops.append(sortvers[i][0])
        choice = random.choice(tops)
        API = Api()
        d = API.getRestaurant(choice)
        return d


    def less_familiar(self, user): # suggestssomething (RETURNS A RESTAURANT NAME) from the bottom 25% of what the user visits
        data = user.getData()
        len_dict = len(data)
        percentage = int(.25 * len_dict)
        sortvers = sorted(data.items(), key=lambda x: x[1])
        tops = []
        for i in range(0, percentage):
            tops.append(sortvers[i][0])
        choice = random.choice(tops)
        API = Api()
        d = API.getRestaurant(choice)
        return d

    def completelynew(self, user): # suggests a cuisine they have never tried before (returns a restaurant name)
        # go through list of all the cuisines that user has tried
        # look at total cuisine list
        # look at cuisines a user hasnt tried
        # pick a random cuisine
        data = user.getData()
        rest_ids = list(data.keys())
        API = Api()
        cuisine_list = []
        for rest_id in rest_ids:
            rest_name = API.getRestaurant(rest_id) # gets the name of the restaurant from the id
            rest = Restaurant(rest_name, user.getCity())
            cuisine_list.append(rest.getRestaurantCuisines())
        cus_list = []
        for str in cuisine_list:  # parses cuisine data and stores all cuisines that user has been to
            x = str.split(", ")
            for ele in x:
                if ele in cus_list:
                    pass
                else:
                    cus_list.append(ele)

        all_cuisines = API.getAllCuisines(user.getCity())
        for c in all_cuisines: # parses cuisine data and finds all cuisines that user has not visited
            if c in cus_list:
                all_cuisines.remove(c)
        choice = random.choice(all_cuisines)
        BIGD = API.fillCuisine(choice, user.getCity()) # given the cuisine name, finds the cuisine id to use with api
        chosen_cuisine = None
        for ele in BIGD:
            temp = ele["cuisine"]
            if temp["cuisine_name"] == choice:
                #print(temp)
                cuisine_id = temp["cuisine_id"]
                chosen_cuisine = Cuisine(choice, cuisine_id)

        rest_data = API.getRestaurantsgivenCuisine(user.getCity(), chosen_cuisine) # list of possible restaurants in json form
        #print(rest_data["results_found"])
        rest_list = []
        for rest in rest_data['restaurants']:
            rest_list.append(rest["restaurant"]["name"])
        fin = random.choice(rest_list)
        return fin
